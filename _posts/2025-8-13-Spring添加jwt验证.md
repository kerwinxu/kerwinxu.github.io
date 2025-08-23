---
layout: post
title: "Spring添加Jwt验证"
date: "2025-08-13"
categories: ["计算机语言", "java"]
---

# 添加依赖
这里仅仅是添加jwt的依赖，jpa和mysql等，在生成spring项目的时候就添加了
```xml
<!-- https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt-impl -->
		<dependency>
		    <groupId>io.jsonwebtoken</groupId>
		    <artifactId>jjwt-impl</artifactId>
		    <version>0.12.5</version>
		    <scope>runtime</scope>
		</dependency>
		<!-- https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt-api -->
		<dependency>
		    <groupId>io.jsonwebtoken</groupId>
		    <artifactId>jjwt-api</artifactId>
		    <version>0.12.5</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt-jackson -->
		<dependency>
		    <groupId>io.jsonwebtoken</groupId>
		    <artifactId>jjwt-jackson</artifactId>
		    <version>0.12.5</version>
		    <scope>runtime</scope>
		</dependency>


```

# 数据库方面
## 实体类
这里仅仅是范例，然后用户是由唯一的角色，如果不是唯一的，得新建一个Role类。

```java
@Entity
@Data
@NoArgsConstructor
@JsonIdentityInfo(
		  generator = ObjectIdGenerators.PropertyGenerator.class,
		  property = "id"
		)
public class User {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;

	@Column(nullable = false)
	private String username;   // 用户名
	@Column(nullable = false)
	private String password;   // 密码


	// 角色
	@Column(nullable = false)
	private String role;

	// 这个用户绑定的部门
	@ManyToOne
	private Department department;


@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (!(obj instanceof User)) return false;
		User user = (User) obj;
		return this.id == user.getId()
				&& this.getUsername() == user.getUsername()
				&& this.getPassword() == user.getPassword()
				&& this.getRole() == user.getRole()
				&& this.getDepartment() == user.getDepartment();
	}
	@Override
	public int hashCode() {
		return (int)this.id;
	}

}

```

## Jpa
```java
public interface UserRepository extends JpaRepository<User, Long>{

    Optional<User> findByUsername(String username);

    boolean existsByUsername(String username);

    // 取得某个部门的所有用户
    Set<User>findByDepartmentId(long departmentId);

}
```

## service
这里仅仅给出结构，实现就不粘贴了。
```java
public interface UserService {


	User Add(User user);    // 增加用户
	User Update(User user); // 更新用户
	boolean Delete(User user); // 删除用户
	Set<User> All();        // 所有的用户

	Set<User> findbyDepartmentId(long departmentId);

	User FindById(long id);   // 查询

	User FindByName(String username);


	boolean isExist(String username); // 用户是否已经存在。

	// 查询某个用户是否拥有某个设备
	boolean isExistUsernameAndDevice(String username, long deviceId);

}


```

# jwt部分
## 小工具
```java
/**
 *
 *
 * JTW 工具类
 */

@Component
public class JwtTokenProvider {

    private static final Logger logger = LoggerFactory.getLogger(JwtTokenProvider.class);

    // 放在spring的配置中了。
    @Value("${app.jwt-secret}")
    private String jwtSecret;

    @Value("${app.jwt-expiration-milliseconds}")
    private long jwtExpirationDate;

    // 生成 JWT token
    public String generateToken(Authentication authentication){
        String username = authentication.getName();

        // 当前时间
        Date currentDate = new Date();
        // 过期时间
        Date expireDate = new Date(currentDate.getTime() + jwtExpirationDate);
        // 添加属性
        Map<String, String> claims = new HashMap<String, String>();

        String token = Jwts.builder()
        		.claims(claims)
                .subject(username)         // 这个用户
                .issuedAt(new Date())      // 这个时间
                .expiration(expireDate)    // 过期时间
                .signWith(key())           // 添加key
                .compact();                // 生成字符串
        return token;
    }




    private Key key(){

//    	return Jwts.SIG.HS256.key().build();
        return Keys.hmacShaKeyFor(
                Decoders.BASE64.decode(jwtSecret)
        );


    }

    // 从 Jwt token 获取用户名
    public String getUsername(String token){
        Claims claims = Jwts.parser()
                .verifyWith((SecretKey) key())
                .build()
                .parseSignedClaims(token)
                .getPayload();
        String username = claims.getSubject();
        return username;
    }

    // 验证 Jwt token
    public boolean validateToken(String token){
        try{
            Jwts.parser()
            		.verifyWith((SecretKey) key())
                    .build()
                    .parse(token);
            return true;
        } catch (MalformedJwtException e) {
            logger.error("Invalid JWT token: {}", e.getMessage());
        } catch (ExpiredJwtException e) {
            logger.error("JWT token is expired: {}", e.getMessage());
        } catch (UnsupportedJwtException e) {
            logger.error("JWT token is unsupported: {}", e.getMessage());
        } catch (IllegalArgumentException e) {
            logger.error("JWT claims string is empty: {}", e.getMessage());
        }
        return false;
    }
}

```
## 自定义用户服务

```java

@Service
@Slf4j
@AllArgsConstructor
public class CustomUserDetailsService implements UserDetailsService {

	@Autowired
	private UserRepository userRepository;
//	private RoleRepository roleRepository;
//	private final PasswordEncoder passwordEncoder;

    @Override
    public UserDetails loadUserByUsername(String usernameOrEmail) throws UsernameNotFoundException {

    	// 查找用户
        User user = userRepository.findByUsername(usernameOrEmail)
                .orElseThrow(() -> new UsernameNotFoundException("User not exists by Username or Email"));

        log.info("the role of current user :" + user.getRole());
        // 我这里仅仅是取得一个角色，实际上可以用Role类，取得多个角色的。
        Set<GrantedAuthority> authorities = Set.of(new SimpleGrantedAuthority(user.getRole()));

        // 返回用户的信息。
        return new org.springframework.security.core.userdetails.User(
                usernameOrEmail,       // 用户名
                user.getPassword(),    // 密码
                authorities            // 角色列表
        );
    }
}
```

## jwt验证连接
这里是验证是否通过验证的
```java
// 拦截传入的 HTTP 请求并验证包含在 Authorization 头中的 JWT Token。如果 Token 有效，Filter 就会在 SecurityContext 中设置当前用户的 Authentication。
@Component
@Slf4j
public class JwtAuthenticationFilter extends OncePerRequestFilter {


	private JwtTokenProvider jwtTokenProvider;


    private UserDetailsService userDetailsService;

    public JwtAuthenticationFilter(JwtTokenProvider jwtTokenProvider2,
			CustomUserDetailsService customUserDetailsService) {
		// TODO Auto-generated constructor stub
    	jwtTokenProvider = jwtTokenProvider2;
    	userDetailsService = customUserDetailsService;

	}

	@Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {

    	log.debug("request" + get_request(request));
        // 从 request 获取 JWT token
        String token = getTokenFromRequest(request);

        log.info("get token :" + token);
        // 校验 token
        if(StringUtils.hasText(token) && jwtTokenProvider.validateToken(token)){
            // 从 token 获取 username
            String username = jwtTokenProvider.getUsername(token);


            // 加载与令 token 关联的用户
            UserDetails userDetails = userDetailsService.loadUserByUsername(username);
            UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(
                userDetails,
                null,
                userDetails.getAuthorities()  // 并且取得他的权限了。
            );

            authenticationToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

            SecurityContextHolder.getContext().setAuthentication(authenticationToken);

        }

        filterChain.doFilter(request, response);
    }

    // 取得
    private String getTokenFromRequest(HttpServletRequest request){

        String bearerToken = request.getHeader(HttpHeaders.AUTHORIZATION);
        log.info("receive bearerToken " + bearerToken);

        String token_startString = "Bearer ";
        if(StringUtils.hasText(bearerToken) && bearerToken.startsWith(token_startString)){
            return bearerToken.substring(token_startString.length(), bearerToken.length());
        }

        return null;
    }

    private String get_request(HttpServletRequest request) {

    	StringBuilder sb = new StringBuilder();

        // 1. 打印基础信息
        sb.append("Method: ").append(request.getMethod()).append("\n");
        sb.append("URL: ").append(request.getRequestURL()).append("\n");
        sb.append("Query String: ").append(request.getQueryString()).append("\n");
        sb.append("Protocol: ").append(request.getProtocol()).append("\n");

        // 2. 打印所有请求头
        sb.append("\nHeaders:\n");
        Enumeration<String> headerNames = request.getHeaderNames();
        while (headerNames.hasMoreElements()) {
            String name = headerNames.nextElement();
            sb.append(name).append(": ").append(request.getHeader(name)).append("\n");
        }

        // 3. 打印所有参数
        sb.append("\nParameters:\n");
        Map<String, String[]> paramMap = request.getParameterMap();
        paramMap.forEach((key, values) -> {
            sb.append(key).append(": ");
            for (String value : values) {
                sb.append(value).append(" ");
            }
            sb.append("\n");
        });

        // 4. 打印客户端信息
        sb.append("\nClient Info:\n");
        sb.append("Remote Addr: ").append(request.getRemoteAddr()).append("\n");
        sb.append("Remote Host: ").append(request.getRemoteHost()).append("\n");
        sb.append("Remote Port: ").append(request.getRemotePort()).append("\n");

        return sb.toString();
    }

}
```

## 验证入口点
```java
//AuthenticationEntryPoint 由 ExceptionTranslationFilter 用来启动身份认证方案。它是一个入口点，用于检查用户是否已通过身份认证，如果用户已经认证，则登录该用户，否则抛出异常（unauthorized）
@Component
public class JwtAuthenticationEntryPoint implements AuthenticationEntryPoint {

    @Override
    public void commence(HttpServletRequest request,
                         HttpServletResponse response,
                         AuthenticationException authException) throws IOException, ServletException {

        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, authException.getMessage());
    }
}
```



## 配置
```java
@Configuration
public class SpringSecurityConfig {

	@Autowired
    private CustomUserDetailsService customUserDetailsService;
    @Autowired
    private JwtTokenProvider jwtTokenProvider;

    @Bean
    public static PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {

        http// 由于使用的是JWT，我们这里不需要csrf
        .csrf(AbstractHttpConfigurer::disable)
        // 禁用跨域检测
//        .cors(AbstractHttpConfigurer:)
        // 禁用session
        .sessionManagement(configurer -> configurer.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        // 权限规则
        .authorizeHttpRequests((authorize) -> {

        	// 放行静态资源（所有非API的请求）
        	authorize.requestMatchers("/**").permitAll()                // 所有的都可以请求
        	.requestMatchers("/api/auth/**").permitAll()                // 验证的也可以请求
        	.requestMatchers(HttpMethod.OPTIONS,"/**").permitAll()      // 有些浏览器在post前会发Option请求，这里一起同意
            .requestMatchers("/api/**").authenticated();                // 这里边的都得东路才能用。
                });
        // JWT 校验过滤器,添加过滤器才能真正的过滤
        http.addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider, customUserDetailsService), UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration configuration) throws Exception {
        return configuration.getAuthenticationManager();
    }
}
```

# 应用

注意两点：
1. 添加 @EnableMethodSecurity注解，然后才会生效
1. 在方法上添加 @PreAuthorize("hasRole('ADMIN')") ，表示得有"ROLE_ADMIN"权限才能生效，注意，权限的前面有"ROLE_"前缀。

```java
@AllArgsConstructor
@RestController
@RequestMapping("/api/userDevice")
//会拦截注解了@PreAuthrize注解的配置.
@EnableMethodSecurity  // 启用方法的验证，启动后，@PreAuthorize才会生效。
@Slf4j
public class UserDeviceController {

	@Autowired
	private UserService userService;

	@Autowired
	private DeviceService deviceService;

	@Autowired
	private UserDeviceService userDeviceService;

	// TODO 建立用户跟设备的关联
	@PreAuthorize("hasRole('ADMIN')")
	@RequestMapping("/add")
	public ResponseEntity<String>addUser(@RequestParam long user_id, @RequestParam long device_id) throws Exception{
		// 这里
		if(userDeviceService.add(user_id, device_id)) {
			return ResponseEntity.ok("成功添加");
		}else {
			return  ResponseEntity.badRequest().body("添加失败");
		}

	}

	// TODO 删除用户跟设备的关联
	@PreAuthorize("hasRole('ADMIN')")
	@RequestMapping("/delete")
	public ResponseEntity<String>deleteUser(@RequestParam long user_id, @RequestParam long device_id) throws Exception{
		// 这里
		if(userDeviceService.delete(user_id, device_id)) {
			return ResponseEntity.ok("成功添加");
		}else {
			return  ResponseEntity.badRequest().body("添加失败");
		}
	}


}
```


# 跨域配置

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;


// 允许跨域的配置
@Configuration
public class CrossOriginWebConfig implements WebMvcConfigurer {
	@Override
	public void addCorsMappings(CorsRegistry registry) {
		registry.addMapping("/**")//项目中的所有接口都支持跨域
        .allowedOriginPatterns("*")//所有地址都可以访问，也可以配置具体地址
        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS") // 允许的方法
        .allowedHeaders("*")
        .allowCredentials(true) // 允许发送凭证（如Cookie）
        .maxAge(3600);// 跨域允许时间
	}
}
```

# web配置
```java
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import PositioningWeb.control.ReportController;
import lombok.extern.slf4j.Slf4j;

@Configuration
@Slf4j
public class WebConfig implements WebMvcConfigurer {


//    @Value("${file.staticAccessPath}")
//    private String staticAccessPath;
//
//    @Value("${file.uploadFolder}")
//    private String uploadFolder;

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        // 获取当前项目运行目录的绝对路径
        String projectPath = System.getProperty("user.dir");
        String uploadPath = projectPath + "/uploads/";
        log.info("项目路径" + projectPath);
        log.info("上传文件保存路径:" + uploadPath);
        // 映射物理路径到虚拟URL路径
        registry.addResourceHandler("/uploads/**")  // 访问路径：http://域名/images/xxx.jpg
                .addResourceLocations("file:" + uploadPath) // 注意 file: 前缀
                .setCachePeriod(3600);
        registry.addResourceHandler("/static/**")
        		.addResourceLocations("classpath:/static/")
        		.setCachePeriod(3600);

        registry.addResourceHandler("/vue/**")
		.addResourceLocations("classpath:/static/vue/")
		.setCachePeriod(3600);
    }

}
```
