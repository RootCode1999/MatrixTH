<template>
  <div>
    <div v-if="is_show == true" class="el-top">您还没有警告信息</div>
    <div class="el-top">
      <el-timeline>
        <el-timeline-item
          v-for="(activity, index) in activities"
          placement="top"
          :key="index"
          :type="activity.type"
          :color="activity.color"
          :size="activity.size"
          :timestamp="activity.timestamp"
        >
          <el-card shadow="hover">
            <p>{{ activity.content }}</p>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      activities: [],
      is_show: false,
    };
  },
  methods: {
    get_warning_arry() {
      var that = this;
      axios
        .get("/get_warning", {
          params: {
            cid: window.localStorage.getItem("cid"),
          },
        })
        .then(function (response) {
          that.activities = response.data.data.warn_arry;
          that.is_show = false;
          if (that.activities.length == 0) {
            var len = that.activities.length;
            console.log(len);
            that.is_show = true;
            console.log(that.is_show);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    this.get_warning_arry();
  },
};
</script>
<style scoped>
.el-top {
  margin-top: 20px;
}
</style>
