---
layout: post
title: "Field passwordEncoder in com.example.demo.Service.CustomUserDetailsService required a bean of type 'org.springframework.security.crypto.password.PasswordEncoder' that could not be found."
date: "2020-08-25"
categories: 
  - "java"
---

出现这个错误，我的解决方式是，给他一个bean不就行了

 

```
@Slf4j
@EnableWebSecurity
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {
  
  @Bean
  public PasswordEncoder passwordEncoder(){
    return new BCryptPasswordEncoder();
  }
  
  @Override
  protected void configure(AuthenticationManagerBuilder auth) throws Exception {
      auth.inMemoryAuthentication()
      .passwordEncoder(passwordEncoder()).withUser("admin")
      .password(passwordEncoder().encode("admin"))
      .roles("ADMIN");
  }

}
```
