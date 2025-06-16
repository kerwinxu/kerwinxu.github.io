---
layout: post
title: "vue-router路由"
date: "2021-02-05"
categories: ["计算机语言", "JavaScript"]
---

# 使用

```
<div id="app">
  <h1>Hello App!</h1>
  <p>
    <!-- 使用 router-link 组件来导航，通过传入 `to` 属性指定链接，<router-link> 默认会被渲染成一个 `<a>` 标签 -->
    <router-link to="/foo">Go to Foo</router-link>
    <router-link to="/bar">Go to Bar</router-link>
  </p>
  <!-- 路由出口，路由匹配到的组件将渲染在这里 -->
  <router-view></router-view>
</div>
<script src="vue.js"></script>
<script src="vue-router.js"></script>
<script>
// 0. 如果使用模块化机制编程，导入Vue和VueRouter，要调用 Vue.use(VueRouter)

// 1. 定义（路由）组件，可以从其他文件 import 进来
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }

// 2. 定义路由
// 每个路由应该映射一个组件。 其中"component" 可以是通过 Vue.extend() 创建的组件构造器，或者，只是一个组件配置对象。
const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

// 3. 创建 router 实例，然后传 `routes` 配置，当然还可以传别的配置参数
const router = new VueRouter({
  routes // （缩写）相当于 routes: routes
})

// 4. 创建和挂载根实例。
// 通过 router 配置参数注入路由，从而让整个应用都有路由功能
const app = new Vue({　　el:'#app',　　router})</script>
```

 

# 重定向和别名

重定向通过 routes 配置来完成，下面例子是从 /a 重定向到 /b

```
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: '/b' }
  ]
})
```

重定向的目标也可以是一个命名的路由：

```
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: { name: 'foo' }}
  ]
})
```

甚至是一个方法，动态返回重定向目标：

```
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: to => {
      // 方法接收 目标路由 作为参数
      // return 重定向的 字符串路径/路径对象      return '/home'
    }}
  ]
})
```

对于不识别的URL地址来说，常常使用重定向功能，将页面定向到首页

```
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
  { path: '*', redirect: "/foo"},
]
```

别名

重定向是指，当用户访问 /a时，URL 将会被替换成 /b，然后匹配路由为 /b，那么别名是什么呢？/a 的别名是 /b，意味着，当用户访问 /b 时，URL 会保持为 /b，但是路由匹配则为 /a，就像用户访问 /a 一样

上面对应的路由配置为

```
const router = new VueRouter({
  routes: [
    { path: '/a', component: A, alias: '/b' }
  ]
})
```

别名』的功能可以自由地将 UI 结构映射到任意的 URL，而不是受限于配置的嵌套路由结构

处理首页访问时，常常将index设置为别名，比如将'/home'的别名设置为'/index'。但是，要注意的是，<router-link to="/home">的样式在URL为/index时并不会显示。因为，router-link只识别出了home，而无法识别index

# 根路径

设置根路径，需要将path设置为'/'

```
<p>
    <router-link to="/">index</router-link>
    <router-link to="/foo">Go to Foo</router-link>
    <router-link to="/bar">Go to Bar</router-link>
  </p>

const routes = [
  { path: '/', component: Home },
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
]
```

但是，由于默认使用的是全包含匹配，即'/foo'、'/bar'也可以匹配到'/'，如果需要精确匹配，仅仅匹配'/'，则需要在router-link中设置exact属性

```
<p>
    <router-link to="/" exact>index</router-link>
    <router-link to="/foo">Go to Foo</router-link>
    <router-link to="/bar">Go to Bar</router-link>
</p>

const routes = [
  { path: '/', component: Home },
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
]
```

# 嵌套路由

顶层的界面如下：

```
<div id="app">
  <p>
    <router-link to="/" exact>index</router-link>
    <router-link to="/foo">Go to Foo</router-link>
    <router-link to="/bar">Go to Bar</router-link>
  </p>
  <router-view></router-view>
</div>
```

 

```
const Home = { template: '<div>home</div>' }
const Foo = { template: `
  <div>
    <p>
      <router-link to="/foo/foo1">to Foo1</router-link>
      <router-link to="/foo/foo2">to Foo2</router-link>
      <router-link to="/foo/foo3">to Foo3</router-link>  
    </p>
    <router-view></router-view>
  </div>
  ` }
const Bar = { template: '<div>bar</div>' }
const Foo1 = { template: '<div>Foo1</div>' }
const Foo2 = { template: '<div>Foo2</div>' }
const Foo3 = { template: '<div>Foo3</div>' }
```

路由设置如下

```
const routes = [
  { path: '/', component: Home },
  { path: '/foo', component: Foo ,children:[
    {path:'foo1',component:Foo1},
    {path:'foo2',component:Foo2},
    {path:'foo3',component:Foo3},
  ]},
  { path: '/bar', component: Bar },
]
```

要特别注意的是，router的构造配置中，children属性里的path属性只设置为当前路径，因为其会依据层级关系；而在router-link的to属性则需要设置为完全路径

如果要设置默认子路由，即点击foo时，自动触发foo1，则需要进行如下修改。将router配置对象中children属性的path属性设置为''，并将对应的router-link的to属性设置为'/foo'

```
const Foo = { template: `
  <div>
    <p>
      <router-link to="/foo" exact>to Foo1</router-link>
      <router-link to="/foo/foo2">to Foo2</router-link>
      <router-link to="/foo/foo3">to Foo3</router-link>  
    </p>
    <router-view></router-view>
  </div>
```

```
const routes = [
  { path: '/', component: Home },
  { path: '/foo', component: Foo ,children:[
    {path:'',component:Foo1},
    {path:'foo2',component:Foo2},
    {path:'foo3',component:Foo3},
  ]},
  { path: '/bar', component: Bar },
]
```

# 命名路由

有时，通过一个名称来标识一个路由显得更方便，特别是在链接一个路由，或者是执行一些跳转时。可以在创建Router实例时，在routes配置中给某个路由设置名称

 

```
const router = new VueRouter({
  routes: [
    {
      path: '/user/:userId',
      name: 'user',
      component: User
    }
  ]
})
```

要链接到一个命名路由，可以给 router-link 的 to 属性传一个对象：

```
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
```

这跟代码调用 router.push() 是一回事

```
router.push({ name: 'user', params: { userId: 123 }})

```

\[注意\]如果设置了默认子路由，则不要在父级路由上设置name属性

```
<div id="app">
  <p>
    <router-link to="/" exact>index</router-link>
    <router-link :to="{ name: 'foo1' }">Go to Foo</router-link>
    <router-link :to="{ name: 'bar' }">Go to Bar</router-link>
  </p>
  <router-view></router-view>
</div>
```

 

```
const Home = { template: '<div>home</div>' }
const Foo = { template: `
  <div>
    <p>
      <router-link :to="{ name: 'foo1' }" exact>to Foo1</router-link>
      <router-link :to="{ name: 'foo2' }" >to Foo2</router-link>
      <router-link :to="{ name: 'foo3' }" >to Foo3</router-link>  
    </p>
    <router-view></router-view>
  </div>
  ` }
const Bar = { template: '<div>bar</div>' }
const Foo1 = { template: '<div>Foo1</div>' }
const Foo2 = { template: '<div>Foo2</div>' }
const Foo3 = { template: '<div>Foo3</div>' }
```

 

```
const routes = [
  { path: '/', name:'home', component: Home },
  { path: '/foo', component: Foo ,children:[
    {path:'',name:'foo1', component:Foo1},
    {path:'foo2',name:'foo2', component:Foo2},
    {path:'foo3',name:'foo3', component:Foo3},
  ]},
  { path: '/bar', name:'bar', component: Bar },
]
```

 

 

# 引用

- [Vue路由vue-router](https://www.cnblogs.com/zwnsyw/p/12307208.html#autoid-0-0-0)
