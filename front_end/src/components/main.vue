<template>
  <el-container style="height: 100vh">
    <el-aside width="auto" style="background-color: #5d6d6b">
      <commonaside></commonaside>
    </el-aside>
    <el-container>
      <el-header>
        <commonheader></commonheader>
      </el-header>
      <el-main class="main-el">
        <router-view> </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import commonaside from "./commonaside.vue";
import commonheader from "./commonheader.vue";
export default {
  name: "main",
  components: {
    commonaside,
    commonheader,
  },
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.el-header {
  background-color: #1fcab3;
}
.main-el {
  padding-top: 0;
}
.el-aside {
  background-color: #545c64;
  height: 100%;
}
</style>
