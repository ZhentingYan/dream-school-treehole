<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1 class="title">梦想教室 树洞</h1>
        <div id="nav">
          <router-link to="/">首页</router-link>
          <router-link to="/post">发布</router-link>
          <router-link to="/info">个人信息</router-link>
        </div>
      </el-header>

      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<style lang="scss">
$header-height: 60px;

html,
body {
  padding: 0;
  margin: 0;
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
  background-color: antiquewhite;
  line-height: 60px;
}
.el-main {
  height: calc(100vh - #{$header-height});
}
h1.title {
  margin: 0;
  float: left;
  margin-left: $header-height;
}
#nav {
  float: right;
  font-size: 1.1em;
  a {
    margin-right: 30px;
  }
}
</style>
