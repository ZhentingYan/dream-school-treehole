<template>
  <div id="app">
    <el-container>
      <el-header>
        <img class="logo" src="@/assets/logo.png" alt="logo" />
        <h1 class="title">梦想教室解忧角</h1>
        <div id="nav">
          <router-link to="/">首页</router-link>
          <router-link to="/post">发布</router-link>
          <a>心愿单</a>
          <router-link to="/info">个人信息</router-link>
        </div>
      </el-header>

      <el-main style="padding:0">
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<style lang="scss">
$header-height: 60px;

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
a {
  text-decoration: none;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.el-header {
  box-shadow: 0 0 1px rgba(0, 0, 0, 0.25);
  line-height: 60px;
}
.el-main {
  height: calc(100vh - #{$header-height});
}
h1.title {
  margin: 0;
  float: left;
}
#nav {
  float: right;
  font-size: 1.1em;
  a {
    margin-right: 30px;
    color: black;
    font-weight: 500;
  }
  .router-link-exact-active {
    border-bottom: 3px solid rgb(243, 201, 33);
  }
}
.logo {
  float: left;
  height: 40px;
  margin: 10px;
  margin-left: $header-height;
}
</style>
