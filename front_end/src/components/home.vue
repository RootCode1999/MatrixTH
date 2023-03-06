<template>
  <div>
    <el-row class="home" :gutter="20">
      <el-col class="left-1" :span="7">
        <el-card shadow="hover">
          <div class="user">
            <img class="user-img" :src="userimage" />
            <div class="user-info">
              <p class="name">{{ username }}</p>
            </div>
          </div>
          <div class="login-info">
            <p>
              登陆时间<span>{{ recentlogindate }}</span>
            </p>
          </div>
        </el-card>
        <el-card
          style="margin-top: 10px; margin-bottom: 10px"
          height="auto"
          shadow="hover"
        >
          <el-table
            :data="tableData"
            highlight-current-row="true"
            style="width: 100%"
          >
            <el-table-column prop="point" label="站点" width="75">
            </el-table-column>
            <el-table-column prop="date" label="时间" width="85">
            </el-table-column>
            <el-table-column prop="temp" label="温度" width="55">
            </el-table-column>
            <el-table-column prop="hum" label="湿度" width="55">
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
      <el-col class="left-1" :span="8">
        <el-card shadow="hover">
          <div id="chart1" style="height: 350px"></div>
          <div class="temp-text">温度-仪表盘(摄氏度)</div>
        </el-card>
        <div
          class="chart-top"
          id="chart3"
          style="height: 280px; width: 400px"
        ></div>
      </el-col>
      <el-col class="left-1" :span="8">
        <el-card shadow="hover">
          <div id="chart2" style="height: 350px"></div>
          <div class="hum-text">湿度-仪表盘(%)</div>
        </el-card>
        <div
          class="chart-top"
          id="chart4"
          style="height: 280px; width: 400px"
        ></div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import axios from "axios";
var echarts = require("echarts");
export default {
  name: "home",
  data() {
    return {
      timer: "",
      userimage: require("../assets/images/user.png"),
      recentlogindate: "2021-01-01",
      username: "LKY",
      useracess: "员工",
      tableData: [
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
        {
          point: "dth1",
          date: "16:44",
          temp: "16",
          hum: "16",
        },
      ],
      option1: {
        series: [
          {
            type: "gauge",
            min: -20,
            max: 60,
            axisLine: {
              lineStyle: {
                width: 20,
                color: [
                  [0.25, "#67e0e3"],
                  [0.7, "#37a2da"],
                  [1, "#fd666d"],
                ],
              },
            },
            pointer: {
              itemStyle: {
                color: "auto",
              },
            },
            axisTick: {
              distance: -20,
              length: 8,
              lineStyle: {
                color: "#fff",
                width: 1,
              },
            },
            splitLine: {
              distance: -30,
              length: 30,
              lineStyle: {
                color: "#fff",
                width: 3,
              },
            },
            axisLabel: {
              color: "auto",
              distance: 30,
              fontSize: 16,
            },
            detail: {
              valueAnimation: true,
              color: "auto",
            },
            data: [
              {
                value: 30.01,
              },
            ],
          },
        ],
      },
      option2: {
        series: [
          {
            type: "gauge",
            axisLine: {
              lineStyle: {
                width: 20,
                color: [
                  [0.25, "#67e0e3"],
                  [0.7, "#37a2da"],
                  [1, "#fd666d"],
                ],
              },
            },
            pointer: {
              itemStyle: {
                color: "auto",
              },
            },
            axisTick: {
              distance: -20,
              length: 8,
              lineStyle: {
                color: "#fff",
                width: 1,
              },
            },
            splitLine: {
              distance: -30,
              length: 30,
              lineStyle: {
                color: "#fff",
                width: 3,
              },
            },
            axisLabel: {
              color: "auto",
              distance: 30,
              fontSize: 16,
            },
            detail: {
              valueAnimation: true,
              color: "auto",
            },
            data: [
              {
                value: 30.01,
              },
            ],
          },
        ],
      },
      option3: {
        title: {
          text: "temperature",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["temperature"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: "{value} °C",
          },
        },
        series: [
          {
            type: "line",
            stack: "Total",
            data: [120, 132, 101, 134, 90, 230, 210],
            smooth: true,
          },
        ],
      },
      option4: {
        title: {
          text: "humidity",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["humidity"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: "{value} %",
          },
        },
        series: [
          {
            type: "line",
            stack: "Total",
            data: [120, 132, 101, 134, 90, 230, 210],
            smooth: true,
            itemStyle: {
              normal: {
                lineStyle: {
                  color: "#00FF00",
                },
              },
            },
          },
        ],
      },
    };
  },
  methods: {
    set1() {
      let myChart = echarts.init(document.getElementById("chart1"));
      myChart.clear(); //如果图表有修改需求建议加上此方法先清后画
      myChart.setOption(this.option1);
    },
    set2() {
      let myChart = echarts.init(document.getElementById("chart2"));
      myChart.clear(); //如果图表有修改需求建议加上此方法先清后画
      myChart.setOption(this.option2);
    },
    set3() {
      let myChart = echarts.init(document.getElementById("chart3"));
      myChart.clear(); //如果图表有修改需求建议加上此方法先清后画
      myChart.setOption(this.option3);
    },
    set4() {
      let myChart = echarts.init(document.getElementById("chart4"));
      myChart.clear(); //如果图表有修改需求建议加上此方法先清后画
      myChart.setOption(this.option4);
    },
    change_value() {
      var that = this;
      axios
        .get("/gettemphumnow")
        .then(function (response) {
          that.option1["series"][0]["data"][0]["value"] =
            response.data.data.temperature;
          that.option2["series"][0]["data"][0]["value"] =
            response.data.data.humidity;
        })
        .catch(function (error) {
          console.log(error);
        });
      let myChart = echarts.init(document.getElementById("chart1"));
      myChart.setOption(this.option1);
      myChart = echarts.init(document.getElementById("chart2"));
      myChart.setOption(this.option2);
    },
    get_value() {
      var that = this;
      axios
        .get("/gettemphumnow")
        .then(function (response) {
          // console.log(response.data);
          that.option1["series"][0]["data"][0]["value"] =
            response.data.data.temperature;
          that.option2["series"][0]["data"][0]["value"] =
            response.data.data.humidity;
          let myChart = echarts.init(document.getElementById("chart1"));
          myChart.setOption(that.option1);
          myChart = echarts.init(document.getElementById("chart2"));
          myChart.setOption(that.option2);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    get_week_history() {
      var that = this;
      axios
        .get("/homegethistory")
        .then(function (response) {
          that.option3["xAxis"]["data"] = response.data.data.date_arry;
          that.option3["series"][0]["data"] =
            response.data.data.temperature_arry;
          let myChart = echarts.init(document.getElementById("chart3"));
          myChart.setOption(that.option3);
          that.option4["xAxis"]["data"] = response.data.data.date_arry;
          that.option4["series"][0]["data"] = response.data.data.humidity_arry;
          myChart = echarts.init(document.getElementById("chart4"));
          myChart.setOption(that.option4);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    get_station() {
      var that = this;
      axios
        .get("/get_station")
        .then(function (response) {
          that.tableData = response.data.data.data;
          //console.log("tabledate");
          //console.log(that.tableData);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    handleResizeChart() {
      let myChart = echarts.init(document.getElementById("chart1"));
      myChart.clear();
      myChart = echarts.init(document.getElementById("chart2"));
      myChart.clear();
      myChart = echarts.init(document.getElementById("chart3"));
      myChart.clear();
      myChart = echarts.init(document.getElementById("chart4"));
      myChart.clear();
    },
    init() {
      this.get_value();
      this.get_week_history();
      this.get_station();
      this.set1();
      this.set2();
      this.set3();
      this.set4();
    },
  },
  mounted() {
    this.init();
    var that = this;
    this.username = window.localStorage.getItem("name");
    this.recentlogindate = window.localStorage.getItem("logintime");
    this.get_station();
    this.timer = setInterval(function () {
      that.change_value();
      that.get_station();
      console.log("Hello");
    }, 2000);
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
};
</script>

<style lang="less" scoped>
.left-1 {
  margin-top: 20px;
}
.user {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
}
.user-img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-right: 40px;
}
.login-info {
  p {
    line-height: 28px;
    font-size: 16px;
    color: #999999;
    span {
      color: #666666;
      margin-left: 60px;
    }
  }
}
.user-info {
  .name {
    font-size: 32px;
    margin-bottom: 10px;
  }
  .access {
    color: #999999;
  }
}
.temp-text {
  align-items: center;
  text-align: center;
  font-size: 20px;
  font-family: "Times New Roman";
  font-weight: 900;
  color: blueviolet;
}
.hum-text {
  align-items: center;
  text-align: center;
  font-size: 20px;
  font-family: "Times New Roman";
  font-weight: 900;
  color: green;
}
.chart-top {
  margin-top: 15px;
}
</style>
