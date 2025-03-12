---
title: "JPA中自定义的插入、更新、删除方法为什么要添加@Modifying注解和@Transactional注解？"
date: "2020-08-25"
categories: 
  - "java"
---

前几天，有个同事在使用JPA的自定义SQL方法时，程序一直报异常，捣鼓了半天也没能解决，咨询我的时候，我看了一眼他的程序，差不多是这个样子的：

```
@Repository
public interface UserRepository extends JpaRepository<User,Long> {
 
    @Query(value = "delete from pro_user where id = ?1",nativeQuery = true)
    void deleteUserById(Long id);
 }
```

我告诉他，你的deleteUserById方法缺少了@Modifying注解和@Transactional注解，他半信半疑地试了一下，然后果然就解决了。其实，如果他查一下官方资料或许很快也就能找到答案。基于这个背景，本文详细讲解一下为何我们自定义的插入、更新、删除操作需要加@Modifying注解和@Transactional注解。

# @Modifying注解

在官方资料中，给出了这样几句说明：

As the queries themselves are tied to the Java method that executes them, you can actually bind them directly by using the Spring Data JPA @Query annotation rather than annotating them to the domain class. You can modify queries that only need parameter binding by annotating the query method with @ModifyingThe @Modifying annotation is only relevant in combination with the @Query annotation. Derived query methods or custom methods do not require this Annotation.Doing so triggers the query annotated to the method as an updating query instead of a selecting one.

如下：

```
@Modifying
@Query("update User u set u.firstname = ?1 where u.lastname = ?2")
int setFixedFirstnameFor(String firstname, String lastname);
```

第一句话的意思是可以用@Query注解来将自定义sql语句绑定到自定义方法上。

第二句话的意思时，可以用@Modifying注解来标注只需要绑定参数的自定义的更新类语句（更新、插入、删除）。

第三名话的意思是说@Modifying只与@Query联合使用，派生类的查询方法和自定义的方法不需要此注解，如：

```
@Repository
public interface UserRepository extends JpaRepository<User,Long> {

    // 父类的保存方法
    @Override
    User save(User entity);

    // 按照JPA语法规则自定义的查询方法
    List<User> findFirst10ByLastname(String lastName, Pageable pageable);
}
```

第四句话的意思是，当加上@Modifying注解时，JPA会以更新类语句来执行，而不再是以查询语句执行。

也就是说，当我们要通过自已写的更新、插入、删除SQL语句来实现更新、插入、删除操作时，至少需要用两个步骤：

1. @Query来注入我们自定义的sql；
2. 使用@Modifying来标注是一个更新类的自定义语句。

按照这个规则，修改同事的那个方法：

```
@Repository
 public interface UserRepository extends JpaRepository<User,Long> {

     @Modifying
     @Query(value = "delete from pro_user where id = ?1",nativeQuery = true)
     void deleteUserById(Long id);
 }
```

但是，此时，该方法还不完整，执行时程序会报以下错误：

```
org.springframework.dao.InvalidDataAccessApiUsageException: Executing an update/delete query; nested exception is javax.persistence.TransactionRequiredException: Executing an update/delete query
    at org.springframework.orm.jpa.EntityManagerFactoryUtils.convertJpaAccessExceptionIfPossible(EntityManagerFactoryUtils.java:402)
    at org.springframework.orm.jpa.vendor.HibernateJpaDialect.translateExceptionIfPossible(HibernateJpaDialect.java:255)
    ......
    at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:70)
Caused by: javax.persistence.TransactionRequiredException: Executing an update/delete query
    at org.hibernate.internal.AbstractSharedSessionContract.checkTransactionNeededForUpdateOperation(AbstractSharedSessionContract.java:398)
    at org.hibernate.query.internal.AbstractProducedQuery.executeUpdate(AbstractProducedQuery.java:1585)
    .......
```

# @Transactional注解

官方的说明：

　　By default, CRUD methods on repository instances are transactional. For read operations, the transaction configuration `readOnly` flag is set to `true`. All others are configured with a plain `@Transactional` so that default transaction configuration applies. For details, see JavaDoc of [`SimpleJpaRepository`](https://docs.spring.io/spring-data/data-jpa/docs/current/api/index.html?org/springframework/data/jpa/repository/support/SimpleJpaRepository.html). If you need to tweak transaction configuration for one of the methods declared in a repository, redeclare the method in your repository interface, as follows:

_Example. Custom transaction configuration for CRUD_

```
public interface UserRepository extends CrudRepository<User, Long> {

  @Override
  @Transactional(timeout = 10)
  public List<User> findAll();

  // Further query method declarations
}
```

这句话的意思是，默认情况下，repository 接口中的CRUD方法都是被@Transactional注解修饰了的，对于读的操作方法，@Transactional注解的readOnly属性是被设置为true的，即只读；CRUD中的其他方法被@Transactional修饰，即非只读。如果你需要修改repository 接口中的某些方法的事务属性，可以在该方法上重新加上@Transactional注解，并设置需要的属性。

我们先来看一下，@Transactional注解的源码：

```
@Target({ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
public @interface Transactional {

    Propagation propagation() default Propagation.REQUIRED;

    Isolation isolation() default Isolation.DEFAULT;

    int timeout() default -1;

    boolean readOnly() default false;

    // 其他省略
}
```

由上可见@Transactional注解的readOnly默认的属性的false，即非只读，当一个事务是非只读事务的时候，我们可以进行任何操作。

再看一下repository 接口的实现类SimpleJpaRepository的源码(只摘了部分源码)：

```
@Repository
@Transactional(
    readOnly = true
)
public class SimpleJpaRepository<T, ID> implements JpaRepositoryImplementation<T, ID> {

    @Transactional
    public void deleteById(ID id) {
        Assert.notNull(id, "The given id must not be null!");
        this.delete(this.findById(id).orElseThrow(() -> {
            return new EmptyResultDataAccessException(String.format("No %s entity with id %s exists!", this.entityInformation.getJavaType(), id), 1);
        }));
    }

    @Transactional
    public void delete(T entity) {
        Assert.notNull(entity, "The entity must not be null!");
        this.em.remove(this.em.contains(entity) ? entity : this.em.merge(entity));
    }

    @Transactional
    public void deleteAll(Iterable<? extends T> entities) {
        Assert.notNull(entities, "The given Iterable of entities not be null!");
        Iterator var2 = entities.iterator();

        while(var2.hasNext()) {
            T entity = var2.next();
            this.delete(entity);
        }
    }

    public T getOne(ID id) {
        Assert.notNull(id, "The given id must not be null!");
        return this.em.getReference(this.getDomainClass(), id);
    }

    public List<T> findAll() {
        return this.getQuery((Specification)null, (Sort)Sort.unsorted()).getResultList();
    }

    public List<T> findAll(@Nullable Specification<T> spec) {
        return this.getQuery(spec, Sort.unsorted()).getResultList();
    }

    public List<T> findAll(@Nullable Specification<T> spec, Sort sort) {
        return this.getQuery(spec, sort).getResultList();
    }

    public <S extends T> long count(Example<S> example) {
        return executeCountQuery(this.getCountQuery(new SimpleJpaRepository.ExampleSpecification(example), example.getProbeType()));
    }

    public <S extends T> boolean exists(Example<S> example) {
        return !this.getQuery(new SimpleJpaRepository.ExampleSpecification(example), example.getProbeType(), (Sort)Sort.unsorted()).getResultList().isEmpty();
    }

    @Transactional
    public <S extends T> S save(S entity) {
        if (this.entityInformation.isNew(entity)) {
            this.em.persist(entity);
            return entity;
        } else {
            return this.em.merge(entity);
        }
    }

    @Transactional
    public <S extends T> S saveAndFlush(S entity) {
        S result = this.save(entity);
        this.flush();
        return result;
    }

    @Transactional
    public void flush() {
        this.em.flush();
    }
}
```

从SimpleJpaRepository源码中可以看出：

1. 　   该类上注解了只读事务@Transactional(readOnly = true)；
2. 该类的所有查询类操作方法都与类相同，都拥有只读事务；
3. 该类的所有保存、更新、删除操作方法都用@Transactional重新注解了（默认readOnly=false）。

说明JPA为我们提供的所有方法，包括JPA规则的自定义方法在其底层都为我们做好了事务处理，而我们自定义的方法需要自己来标注事务的类型是只读还是非只读。根据这个原理，再次修改开篇所列出的方法：

```
@Repository
public interface UserRepository extends JpaRepository<User,Long> {

    @Transactional
    @Modifying
    @Query(value = "delete from pro_user where id = ?1",nativeQuery = true)
    void deleteUserById(Long id);
}
```

至此，该方法按所期望的结果运行成功了。

# @Modifying注解补充说明

```
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.METHOD, ElementType.ANNOTATION_TYPE })
@Documented
public @interface Modifying {

    boolean flushAutomatically() default false;

    boolean clearAutomatically() default false;
}
```

该注解中有两个属性：flushAutomatically、clearAutomatically，从字面理解是自动刷新和自动清除。

自动刷新，即执行完语句后立即将变化内容刷新到磁盘，如果是insert语句操作，则与JPA的<S extends T> S saveAndFlush(S entity);方法效果相同；

自动清除，即执行完语句后自动清除掉已经过期的实体，比如，我们删除了一个实体，但是在还没有执行flush操作时，这个实体还存在于实体管理器EntityManager中，但这个实体已经过期没有任何用处，直到flush操作时才会被删除掉。如果希望在删除该实体时立即将该实体从实体管理器中删除，则可以将该属性设置为true，如：

```
@Modifying(clearAutomatically = true)
    @Transactional
    @Query(value = "delete from pro_user where id = ?1",nativeQuery = true)
    void deleteUserById(Long id);
```
