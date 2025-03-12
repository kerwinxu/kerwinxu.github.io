---
layout: post
title: "spring的jpa总结"
date: "2021-01-02"
categories: 
  - "java"
---

# 关系映射

## @OneToOne关系映射

实体 People ：用户。

实体 Address：家庭住址。

People 和 Address 是一对一的关系。

这里用两种方式描述JPA的一对一关系。

一种是通过外键的方式(一个实体通过外键关联到另一个实体的主键)；

另外一种是通过一张关联表来保存两个实体一对一的关系。

### 通过外键的形式

people 表（id，name，sex，birthday，address\_id）

address 表（id，phone，zipcode，address）

People.java

```
@Entity
public class People {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Long id;//id
    @Column(name = "name", nullable = true, length = 20)
    private String name;//姓名
    @Column(name = "sex", nullable = true, length = 1)
    private String sex;//性别
    @Column(name = "birthday", nullable = true)
    private Timestamp birthday;//出生日期
    @OneToOne(cascade=CascadeType.ALL)//People是关系的维护端，当删除 people，会级联删除 address
    @JoinColumn(name = "address_id", referencedColumnName = "id")//people中的address_id字段参考address表中的id字段
    private Address address;//地址
}
```

 

关联的实体的主键一般是用来做外键的。但如果此时不想主键作为外键，则需要设置referencedColumnName属性。当然这里关联实体(Address)的主键 id 是用来做主键，所以这里第20行的 referencedColumnName = "id" 实际可以省略。

Address.java

```
@Entity
public class Address {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Long id;//id
    @Column(name = "phone", nullable = true, length = 11)
    private String phone;//手机
    @Column(name = "zipcode", nullable = true, length = 6)
    private String zipcode;//邮政编码
    @Column(name = "address", nullable = true, length = 100)
    private String address;//地址
    //如果不需要根据Address级联查询People，可以注释掉
//    @OneToOne(mappedBy = "address", cascade = {CascadeType.MERGE, CascadeType.REFRESH}, optional = false)
//    private People people;
}
```

### 通过关联表的方式来保存一对一的关系

people 表（id，name，sex，birthday）

address 表 (id，phone，zipcode，address）

people\_address (people\_id，address\_id)

只需要创建 People 和 Address 两个实体

 

People.java

```
@Entity
public class People {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Long id;//id
    @Column(name = "name", nullable = true, length = 20)
    private String name;//姓名
    @Column(name = "sex", nullable = true, length = 1)
    private String sex;//性别
    @Column(name = "birthday", nullable = true)
    private Timestamp birthday;//出生日期
    @OneToOne(cascade=CascadeType.ALL)//People是关系的维护端
    @JoinTable(name = "people_address",
            joinColumns = @JoinColumn(name="people_id"),
            inverseJoinColumns = @JoinColumn(name = "address_id"))//通过关联表保存一对一的关系
    private Address address;//地址
}
```

Address.java

不变

## @OneToMany 和 @ManyToOne

实体 Author：作者。

实体 Article：文章。

Author 和 Article 是一对多关系(双向)。那么在JPA中，如何表示一对多的双向关联呢？

JPA使用@OneToMany和@ManyToOne来标识一对多的双向关联。一端(Author)使用@OneToMany,多端(Article)使用@ManyToOne。

在JPA规范中，一对多的双向关系由多端(Article)来维护。就是说多端(Article)为关系维护端，负责关系的增删改查。一端(Author)则为关系被维护端，不能维护关系。

一端(Author)使用@OneToMany注释的mappedBy="author"属性表明Author是关系被维护端。

多端(Article)使用@ManyToOne和@JoinColumn来注释属性 author,@ManyToOne表明Article是多端，@JoinColumn设置在article表中的关联字段(外键)。

 

Author.java

```
@Entity
public class Author {
    @Id // 主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 自增长策略
    private Long id; //id
    @NotEmpty(message = "姓名不能为空")
    @Size(min=2, max=20)
    @Column(nullable = false, length = 20)
    private String name;//姓名
    @OneToMany(mappedBy = "author",cascade=CascadeType.ALL,fetch=FetchType.LAZY)
    //级联保存、更新、删除、刷新;延迟加载。当删除用户，会级联删除该用户的所有文章
    //拥有mappedBy注解的实体类为关系被维护端
     //mappedBy="author"中的author是Article中的author属性
    private List<Article> articleList;//文章列表
}
```

Article.java

```
@Entity
public class Article {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 自增长策略
    @Column(name = "id", nullable = false)
    private Long id;
    @NotEmpty(message = "标题不能为空")
    @Size(min = 2, max = 50)
    @Column(nullable = false, length = 50) // 映射为字段，值不能为空
    private String title;
    @Lob  // 大对象，映射 MySQL 的 Long Text 类型
    @Basic(fetch = FetchType.LAZY) // 懒加载
    @NotEmpty(message = "内容不能为空")
    @Size(min = 2)
    @Column(nullable = false) // 映射为字段，值不能为空
    private String content;//文章全文内容
    @ManyToOne(cascade={CascadeType.MERGE,CascadeType.REFRESH},optional=false)//可选属性optional=false,表示author不能为空。删除文章，不影响用户
    @JoinColumn(name="author_id")//设置在article表中的关联字段(外键)
    private Author author;//所属作者
}
```

**最终生成的表结构**

article 表(id，title，conten，**author\_id**)

author 表(**id**，name)

 

## @ManyToMany 多对多

实体 User：用户。

实体 Authority：权限。

用户和权限是多对多的关系。一个用户可以有多个权限，一个权限也可以被很多用户拥有。

JPA中使用@ManyToMany来注解多对多的关系，由一个关联表来维护。这个关联表的表名默认是：主表名+下划线+从表名。(主表是指关系维护端对应的表,从表指关系被维护端对应的表)。这个关联表只有两个外键字段，分别指向主表ID和从表ID。字段的名称默认为：主表名+下划线+主表中的主键列名，从表名+下划线+从表中的主键列名。

 

需要注意的：

1、多对多关系中一般不设置级联保存、级联删除、级联更新等操作。

2、可以随意指定一方为关系维护端，在这个例子中，我指定 User 为关系维护端，所以生成的关联表名称为： user\_authority，关联表的字段为：user\_id 和 authority\_id。

3、多对多关系的绑定由关系维护端来完成，即由 User.setAuthorities(authorities) 来绑定多对多的关系。关系被维护端不能绑定关系，即Game不能绑定关系。

4、多对多关系的解除由关系维护端来完成，即由Player.getGames().remove(game)来解除多对多的关系。关系被维护端不能解除关系，即Game不能解除关系。

5、如果 User 和 Authority 已经绑定了多对多的关系，那么不能直接删除 Authority，需要由 User 解除关系后，才能删除 Authority。但是可以直接删除 User，因为 User 是关系维护端，删除 User 时，会先解除 User 和 Authority 的关系，再删除 Authority。

 

User.java

```
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @NotEmpty(message = "账号不能为空")
    @Size(min=3, max=20)
    @Column(nullable = false, length = 20, unique = true)
    private String username; // 用户账号，用户登录时的唯一标识
    @NotEmpty(message = "密码不能为空")
    @Size(max=100)
    @Column(length = 100)
    private String password; // 登录时密码
    @ManyToMany
    @JoinTable(name = "user_authority",joinColumns = @JoinColumn(name = "user_id"),
    inverseJoinColumns = @JoinColumn(name = "authority_id"))
    //1、关系维护端，负责多对多关系的绑定和解除
    //2、@JoinTable注解的name属性指定关联表的名字，joinColumns指定外键的名字，关联到关系维护端(User)
    //3、inverseJoinColumns指定外键的名字，要关联的关系被维护端(Authority)
    //4、其实可以不使用@JoinTable注解，默认生成的关联表名称为主表表名+下划线+从表表名，
    //即表名为user_authority
    //关联到主表的外键名：主表名+下划线+主表中的主键列名,即user_id
    //关联到从表的外键名：主表中用于关联的属性名+下划线+从表的主键列名,即authority_id
    //主表就是关系维护端对应的表，从表就是关系被维护端对应的表
    private List<Authority> authorityList;
}
```

 

注意：如注释中所言，上面的第19-20行的@JoinTable可以省略，默认可以生成

Authority.java

```
@Entity
public class Authority {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(nullable = false)
    private String name; //权限名
    @ManyToMany(mappedBy = "authorityList")
    private List<User> userList;
}
```

 

测试 添加

```
@SpringBootTest
@RunWith(SpringRunner.class)
public class UserRepositoryTest {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private AuthorityRepository authorityRepository;
    @Test
    public void saveAuthority() {
        Authority authority = new Authority();
        authority.setId(1);
        authority.setName("ROLE_ADMIN");
        authorityRepository.save(authority);
    }
    @Test
    public void saveUser() {
        User user = new User();
        user.setUsername("admin");
        user.setPassword("123456");
        Authority authority = authorityRepository.findById(1).get();
        List<Authority> authorityList = new ArrayList<>();
        authorityList.add(authority);
        user.setAuthorList(authorityList);
        userRepository.save(user);
    }
}
```

先运行 saveAuthority 添加一条权限记录，

然后运行 saveUser 添加一条用户记录，与此同时，user\_authority 表中也自动插入了一条记录

 

**测试 删除**

删除用户

```
@SpringBootTest
@RunWith(SpringRunner.class)
public class UserRepositoryTest {
    @Autowired
    private UserRepository userRepository;
    @Test
    public void deleteUser() {
        userRepository.deleteById(1L);
    }
}
```

user 表中删除一条记录，同时 user\_authority 能够级联删除一条记录

## 补充

其中 @OneToMany  和 @ManyToOne 用得最多，这里再补充一下

 

关于级联，一定要注意，要在关系的维护端，即 One 端。

比如 作者和文章，作者是One，文章是Many；文章和评论，文章是One，评论是Many。

**cascade = CascadeType.ALL 只能写在 One 端，只有One端改变Many端，不准Many端改变One端。**

特别是删除，因为 ALL 里包括更新，删除。

如果删除一条评论，就把文章删了，那算谁的。所以，在使用的时候要小心。一定要在 One 端使用。

 

ManytoMany的，两个类都要重写tostring，避免无限递归。

# 引用

- [Spring Data JPA 之 一对一，一对多，多对多 关系映射](https://blog.csdn.net/johnf_nash/article/details/80642581)
