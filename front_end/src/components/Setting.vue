<template>
  <div>
    <el-card class="el-top" style="width: 650px" shadow="never">
      <div class="temp-card" style="width: 600px">
        <div class="temp-title">温度阈值设置</div>
        <el-input
          class="el-top"
          placeholder="请输入温度(°C)"
          v-model="temp_top_input"
        >
          <div class="temp-text" slot="prepend">请输入温度上限</div>
        </el-input>
        <el-input
          class="el-top"
          placeholder="请输入温度(°C)"
          v-model="temp_low_input"
        >
          <div class="temp-text" slot="prepend">请输入温度下限</div>
        </el-input>
        <div class="button-layout">
          <div />
          <el-button
            class="button-display"
            type="primary"
            @click="send_temperature"
            >确认</el-button
          >
        </div>
      </div>
    </el-card>
    <el-card class="el-top" style="width: 650px" shadow="never">
      <div class="temp-card" style="width: 600px">
        <div class="hum-title">湿度阈值设置</div>
        <el-input
          class="el-top"
          placeholder="请输入湿度(%)"
          v-model="hum_top_input"
        >
          <div class="temp-text" slot="prepend">请输入湿度上限</div>
        </el-input>
        <el-input
          class="el-top"
          placeholder="请输入湿度(%)"
          v-model="hum_low_input"
        >
          <div class="temp-text" slot="prepend">请输入湿度下限</div>
        </el-input>
        <div class="button-layout">
          <div />
          <el-button
            class="button-display"
            type="primary"
            @click="send_humidity"
            >确认</el-button
          >
        </div>
      </div>
    </el-card>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      temp_top_input: "",
      temp_low_input: "",
      hum_top_input: "",
      hum_low_input: "",
      cid: "",
    };
  },
  methods: {
    get_cid() {
      var local_cid = window.localStorage.getItem("cid");
      this.cid = local_cid;
    },
    send_temperature() {
      //var that = this;
      if (this.temp_top_input.length == 0) {
        alert("请设置温度上限");
        return;
      }
      if (this.temp_low_input.length == 0) {
        alert("请设置温度下限");
        return;
      }
      if (parseInt(this.temp_low_input) > parseInt(this.temp_top_input)) {
        alert("请检查温度设置");
        return;
      }
      axios
        .get("/set_temperature_threshold", {
          params: {
            temp_top: this.temp_top_input,
            temp_low: this.temp_low_input,
            cid: window.localStorage.getItem("cid"),
          },
        })
        .then(function (response) {
          console.log(response.data);

          if (response.data.status == 0) {
            alert("温度阈值设置成功");
          } else {
            alert("温度阈值设置失败：" + response.data.msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    send_humidity() {
      //var that = this;
      if (this.hum_top_input.length == 0) {
        alert("请设置湿度上限");
        return;
      }
      if (this.hum_low_input.length == 0) {
        alert("请设置湿度下限");
        return;
      }
      if (parseInt(this.hum_low_input) > parseInt(this.hum_top_input)) {
        alert("请检查湿度设置");
        return;
      }
      axios
        .get("/set_humidity_threshold", {
          params: {
            hum_top: this.hum_top_input,
            hum_low: this.hum_low_input,
            cid: window.localStorage.getItem("cid"),
          },
        })
        .then(function (response) {
          console.log(response.data);
          if (response.data.status == 0) {
            alert("湿度阈值设置成功");
          } else {
            alert("湿度阈值设置失败：" + response.data.msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    this.get_cid();
  },
};
</script>
<style scoped>
.el-top {
  margin-top: 20px;
}
.temp-card {
  margin-top: 20px;
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
}
.temp-title {
  font-size: 20px;
  color: #d00000;
  font-weight: 600;
  font-family: "Brush Script Std";
}
.temp-text {
  color: black;
  font-weight: 550;
}
.button-display {
  margin-top: 20px;
  margin-left: 530px;
}
.button-layout {
  display: flex;
}
.hum-title {
  font-size: 20px;
  color: #52b69a;
  font-weight: 600;
  font-family: "Brush Script Std";
}
</style>
