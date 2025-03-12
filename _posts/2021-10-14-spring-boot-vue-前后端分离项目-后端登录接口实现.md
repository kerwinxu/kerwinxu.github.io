---
title: "Spring Boot + Vue 前后端分离项目 -- 后端登录接口实现"
date: "2021-10-14"
categories: 
  - "java"
---

# 要点

- 前端通过axis 访问后端，后端提供给前端信息，但后端返回的页面信息，浏览器并不会根据这个信息重新刷新页面，决定权在前端手中。
    - 比如登录配置中 and().formLogin().loginPage("/users/login\_page") // 登录的页面，实际上前端登录的页面很可能不是这个路径，后端可能会将这个信息发送给前端，但前端很可能不理，前端有自己的登录页面。
- 自定义各种接口，包括如下
    - SimpleUrlAuthenticationSuccessHandler ： 登录成功返回的信息
    - SimpleUrlAuthenticationFailureHandler ： 登录失败返回的信息
    - AuthenticationEntryPoint ： 异常返回的信息
    - SimpleUrlLogoutSuccessHandler ： 登出成功返回的信息
- 配置，在public class SecurityConfiguration extends WebSecurityConfigurerAdapter中配置，要加上注解@Configurable 和 @EnableWebSecurity
    - public void configure(WebSecurity webSecurity) 资源配置
    - protected void configure(HttpSecurity http) throws Exception ，这个是http请求的配置。
    - protected void configure(AuthenticationManagerBuilder auth) throws Exception ， 这个是访问的配置。

# 例子如下：

后端配置代码：

```
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;
import org.springframework.security.authentication.AuthenticationDetailsSource;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.AuthenticationEntryPoint;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;
import org.springframework.security.web.authentication.WebAuthenticationDetails;
import org.springframework.security.web.authentication.logout.SimpleUrlLogoutSuccessHandler;

import com.bocsh.mer.security.MyUserDetailsService;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Autowired
    MyUserDetailsService myDetailService;
    
    @Autowired
    private AuthenticationDetailsSource<HttpServletRequest, WebAuthenticationDetails> authenticationDetailsSource;
    
    protected Log log = LogFactory.getLog(this.getClass());
    
    @Autowired
    private AuthenticationProvider authenticationProvider; 

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        
        auth.authenticationProvider(authenticationProvider);
    }
    
    //定义登陆成功返回信息
    private class AjaxAuthSuccessHandler extends SimpleUrlAuthenticationSuccessHandler {
        @Override
        public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
            
            //User user = (User)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
            log.info("商户[" + SecurityContextHolder.getContext().getAuthentication().getPrincipal() +"]登陆成功！");
            //登陆成功后移除session中验证码信息
            request.getSession().removeAttribute("codeValue");
            request.getSession().removeAttribute("codeTime");
            
            response.setContentType("application/json;charset=utf-8");
            PrintWriter out = response.getWriter();
            out.write("{\"status\":\"ok\",\"msg\":\"登录成功\"}");
            out.flush();
            out.close();
        }
    }
    
    //定义登陆失败返回信息
    private class AjaxAuthFailHandler extends SimpleUrlAuthenticationFailureHandler {
        @Override
        public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
            //登陆失败后移除session中验证码信息
            request.getSession().removeAttribute("codeValue");
            request.getSession().removeAttribute("codeTime");
            
            response.setContentType("application/json;charset=utf-8");
            response.setStatus(HttpStatus.UNAUTHORIZED.value());
            PrintWriter out = response.getWriter();
            out.write("{\"status\":\"error\",\"msg\":\"请检查用户名、密码或验证码是否正确\"}");
            out.flush();
            out.close();
        }
    }
    
    //定义异常返回信息
    public class UnauthorizedEntryPoint implements AuthenticationEntryPoint {
        @Override
        public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException {
            response.sendError(HttpStatus.UNAUTHORIZED.value(),authException.getMessage());
        }

    }
    
    //定义登出成功返回信息
    private class AjaxLogoutSuccessHandler extends SimpleUrlLogoutSuccessHandler  {

        public void onLogoutSuccess(HttpServletRequest request, HttpServletResponse response,
                Authentication authentication) throws IOException, ServletException {
            response.setContentType("application/json;charset=utf-8");
            PrintWriter out = response.getWriter();
            out.write("{\"status\":\"ok\",\"msg\":\"登出成功\"}");
            out.flush();
            out.close();
        }
    }
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
        .exceptionHandling().authenticationEntryPoint(new UnauthorizedEntryPoint())
        .and()
        .csrf().disable()
        .authorizeRequests()                   
            .antMatchers("/users/login_page","/users/captcha").permitAll()
            .anyRequest().authenticated()
            .and().formLogin().loginPage("/users/login_page")
                              .successHandler(new AjaxAuthSuccessHandler())
                              .failureHandler(new AjaxAuthFailHandler())
                              .loginProcessingUrl("/login")
                              .authenticationDetailsSource(authenticationDetailsSource)
            .and()
            .logout().logoutSuccessHandler(new AjaxLogoutSuccessHandler())
            .logoutUrl("/logout");
    }
}
```

前端代码：

```
instance.interceptors.response.use(res => {
      let { data } = res
      this.destroy(url)
      if (this.shade) {
        Spin.hide()
        Modal.success({
          title: '操作成功'
        })
      }
      console.log(res)
      return data
    }, error => {
      console.log(error)
      var code = error.response.status
      if (code === 401) {
        Cookies.remove(TOKEN_KEY)
        window.location.href = '/login'
        Message.error('未登录，或登录失效，请登录')
      }
```

这里面我们定义了一个响应拦截器，在error情况下，判断若返回码为401（就是我们在spring security中自定义的handler的错误状态码），则自动跳转至登陆页面。这样实现了在会话失效的情况下，点击前端任意需要访问后端api的按钮，均会触发跳转登录首页的效果，符合我们的预期。实际情况中一般前端框架都会自己带一套基于cookies的认证机制，这里我们把cookies的失效时间可以设置的长一点（一般可以设为一天），以保障还是以后端会话的失效时间为准。

 

# 引用

- [使用vue集成spring security进行安全登陆](https://www.jianshu.com/p/62a0a9a78530)
- [Spring Boot + Vue 前后端分离项目 -- 后端登录接口实现](https://www.cnblogs.com/youcoding/p/14729173.html)
