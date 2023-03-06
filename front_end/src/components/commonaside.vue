<template>
  <div>
    <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      background-color="#5d6d6b"
      text-color="#fff"
      active-text-color="#ffd04b"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollapse"
      style="border-right: 0px"
    >
      <h3 class="head-text">{{ isCollapse ? "后台" : "温湿度云分析平台" }}</h3>
      <el-menu-item
        v-for="item in nochildren"
        :index="item.pos"
        :key="item.path"
        @click="clickmenu(item)"
      >
        <i :class="'el-icon-' + item.icon"></i>
        <span slot="title">{{ item.label }}</span>
      </el-menu-item>

      <!-- <el-submenu
        v-for="item in haschildren"
        :index="item.path"
        :key="item.path"
      >
        <template slot="title">
          <i :class="'el-icon-' + item.icon"></i>
          <span slot="title">{{ item.label }}</span>
        </template>
        <el-menu-item-group
          v-for="(subitem, subindex) in item.children"
          :key="subitem.path"
        >
          <el-menu-item :index="subindex">{{ subitem.label }}</el-menu-item>
        </el-menu-item-group>
      </el-submenu> -->
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          pos: "1",
          path: "/",
          name: "home",
          label: "首页",
          icon: "s-home",
        },
        {
          pos: "2",
          path: "/history",
          name: "history",
          label: "历史记录与预测",
          icon: "video-play",
        },
        {
          pos: "3",
          path: "/setting",
          name: "setting",
          label: "阈值设置",
          icon: "setting",
        },
        {
          pos: "4",
          path: "/warning",
          name: "warning",
          label: "警告信息",
          icon: "lightning",
        },
      ],
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    jump(num) {
      if (num == 1) {
        this.$router.push({ name: "home" });
      }
    },
    clickmenu(item) {
      this.$router.push({ name: item.name });
    },
  },
  computed: {
    nochildren: function () {
      return this.menu.filter((item) => !item.children);
    },
    haschildren: function () {
      return this.menu.filter((item) => item.children);
    },
    isCollapse() {
      return this.$store.state.isCollapse;
    },
  },
};
</script>

<style>
.el-menu-vertical-demo {
  width: 200px;
  min-height: 100%;
  border: none;
}
.head-text {
  text-align: center;
  color: aquamarine;
}
</style>
