<template>
  <header>
    <div class="l-content">
      <!-- <el-button
        @click="handlemenu"
        class="el-button-demo"
        plain
        icon="el-icon-menu"
        size="mini"
      ></el-button> -->
      <h4 style="color: white">MatrixTH</h4>
    </div>
    <div class="r-content">
      <el-button type="success" @click="backToHome">退出</el-button>
    </div>
  </header>
</template>

<script>
export default {
  name: "commonheader",
  data() {
    return {
      userimage: require("../assets/images/user.png"),
    };
  },
  methods: {
    handlemenu() {
      this.$store.commit("collapsemenu");
    },
    backToHome() {
      this.$router.push({
        path: "/",
      });
    },
  },
};
</script>

<style lang="less" scoped>
header {
  display: flex;
  height: 100%;
  justify-content: space-between;
  align-items: center;
}
.l-content {
  display: flex;
  align-items: center;
}
.el-button-demo {
  margin-right: 20px;
}
.user {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
</style>
