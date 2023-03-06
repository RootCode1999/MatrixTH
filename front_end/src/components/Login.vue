//登录

<template>
  <div class="login" id="login" @keyup.enter="login">
    <!--    <a href="javascript:;" class="log-close"><i class="icons close"></i></a>-->
    <div class="reg-bg">
      <div class="log-cloud cloud1"></div>
      <div class="log-cloud cloud2"></div>
      <div class="log-cloud cloud3"></div>
      <div class="log-cloud cloud4"></div>

      <div class="log-logo" @click="backToHome">
        Welcome Back!<br />MatrixTH
      </div>
    </div>
    <div class="log-email">
      <input
        type="text"
        placeholder="Name"
        class="log-input"
        v-model="username"
      />
      <input
        type="password"
        placeholder="Password"
        class="log-input"
        v-model="password"
      />

      <div class="errorMessage">{{ errorMessage }}</div>
      <a href="javascript:;" class="log-btn" @click="login">登录</a>
      <a href="javascript:;" class="log-btn" @click="reg">注册</a>
    </div>
  </div>
</template>

<script>
// import crypto from "crypto";
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      isLoging: false,
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    //邮件和密码的格式验证
    // patternMatching(mail, pa) {
    //   //Email地址
    //   let mail_pattern = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\w+([-.]\w+)*$/;
    //   //密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)
    //   let password_pattern = /^\w{6,18}$/;
    //   if (mail_pattern.test(mail) == false) {
    //     console.log("mail_pattern error");
    //     this.errorMessage = "邮件格式错误";
    //     return false;
    //   } else if (password_pattern.test(pa) == false) {
    //     console.log("password_pattern error");
    //     if (pa.length < 6 || pa.length == 0) {
    //       this.errorMessage = "密码长度必须大于5";
    //     } else if (pa.length > 18) {
    //       this.errorMessage = "密码长度必须小于18";
    //     } else {
    //       this.errorMessage = "密码只能含有字母、数字、下划线";
    //     }
    //     return false;
    //   } else {
    //     return true;
    //   }
    // },
    login() {
      // if (this.patternMatching(this.userID, this.password) == false) {
      //   return;
      // }
      //md5加密
      // const md5 = crypto.createHash("md5");
      // md5.update(this.password);
      // let md5password = md5.digest("hex");
      var that = this;
      axios
        .get("/login", {
          params: {
            name: this.username,
            passwd: this.password,
          },
        })
        .then(function (response) {
          console.log(response.data);

          if (response.data.status == 0) {
            that.$store.commit("setcusname", response.data.data["cname"]);
            that.$store.commit("setlogintime", response.data.data["logintime"]);
            var name = that.$store.state.cusname;
            var logintime = that.$store.state.logintime;
            var cid = response.data.data["cid"];
            window.localStorage.setItem("name", name);
            window.localStorage.setItem("logintime", logintime);
            window.localStorage.setItem("cid", cid);
            that.$router.push({ path: "/main/home" });
          } else {
            alert("登录失败，原因：" + response.data.msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    //跳转至注册页面
    reg() {
      let _this = this;
      _this.$router.push({
        path: "/Register",
      });
    },
    backToHome() {
      this.$router.push({
        path: "/",
      });
    },
  },
};
</script>

<style scoped>
.errorMessage {
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
  color: #f88787;
}
.login {
  position: absolute;
  overflow: hidden;
  left: 50%;
  margin-left: -250px;
  top: 3%;
  width: 500px;
  min-height: 555px;
  margin-bottom: 3%;
  padding-bottom: 30px;
  z-index: 10;
  background: #fff;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  -webkit-box-shadow: 0px 3px 16px -5px #070707;
  box-shadow: 0px 3px 16px -5px #070707;
}
.log-close {
  display: block;
  position: absolute;
  top: 12px;
  right: 12px;
  opacity: 1;
}
.log-close:hover .icons {
  transform: rotate(180deg);
}
.log-close .icons {
  opacity: 1;
  transition: all 0.3s;
}
.log-cloud {
  background-image: url(../assets/login-cloud.png);
  width: 63px;
  height: 40px;
  position: absolute;
  z-index: 1;
}
.login .cloud1 {
  top: 21px;
  left: -30px;
  transform: scale(0.6);
  animation: cloud1 20s linear infinite;
}
.login .cloud2 {
  top: 87px;
  right: 20px;
  animation: cloud2 19s linear infinite;
}
.login .cloud3 {
  top: 160px;
  left: 5px;
  transform: scale(0.8);
  animation: cloud3 21s linear infinite;
}
.login .cloud4 {
  top: 150px;
  left: -40px;
  transform: scale(0.4);
  animation: cloud4 19s linear infinite;
}
.reg-bg {
  background: url(../assets/login-bg.jpg);
  width: 100%;
  height: 312px;
  overflow: hidden;
}
/*color: #1fcab3;*/
.log-logo {
  height: 80px;
  margin: 120px auto 25px;
  text-align: center;
  color: #1fcab3;
  font-weight: bold;
  font-size: 40px;
  cursor: pointer;
}
.log-text {
  color: #57d4c3;
  font-size: 13px;
  text-align: center;
  margin: 0 auto;
}
.log-logo,
.log-text {
  z-index: 2;
}
.icons {
  background: url(../assets/icons.png) no-repeat;
  display: inline-block;
}
.close {
  height: 16px;
  width: 16px;
  background-position: -13px 0;
}
.login-email {
  height: 17px;
  width: 29px;
  background-position: -117px 0;
}

.log-btns {
  padding: 15px 0;
  margin: 0 auto;
}
.log-btn {
  width: 402px;
  display: block;
  text-align: left;
  line-height: 50px;
  margin: 0 auto 15px;
  height: 50px;
  color: #fff;
  font-size: 13px;
  -webkit-border-radius: 5px;
  background-color: #3b5999;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
  position: relative;
}
.log-btn.tw {
  background-color: #13b4e9;
}
.log-btn.email {
  background-color: #50e3ce;
}
.log-btn:hover,
.log-btn:focus {
  color: #fff;
  opacity: 0.8;
}

.log-email {
  text-align: center;
  margin-top: 20px;
}
.log-email #findPassHref {
  text-align: right;
  margin-right: 50px;
  margin-bottom: 20px;
  font-size: 1px;
  color: #50e3ce;
}
#findPassHref span {
  cursor: pointer;
}
.log-email .log-btn {
  background-color: #50e3ce;
  text-align: center;
}
.log-input-empty {
  border: 1px solid #f37474 !important;
}
.isloading {
  background: #d6d6d6;
}
.log-btn .icons {
  margin-left: 30px;
  vertical-align: middle;
}
.log-btn .text {
  left: 95px;
  line-height: 50px;
  text-align: left;
  position: absolute;
}
.log-input {
  width: 370px;
  overflow: hidden;
  padding: 0 15px;
  font-size: 13px;
  border: 1px solid #ebebeb;
  margin: 0 auto 15px;
  height: 48px;
  line-height: 48px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  -o-border-radius: 5px;
  border-radius: 5px;
}
.log-input.warn {
  border: 1px solid #f88787;
}

@-webkit-keyframes cloud1 {
  0% {
    left: 200px;
  }
  100% {
    left: -130px;
  }
}
@keyframes cloud1 {
  0% {
    left: 200px;
  }
  100% {
    left: -130px;
  }
}

@-webkit-keyframes cloud2 {
  0% {
    left: 500px;
  }
  100% {
    left: -90px;
  }
}
@keyframes cloud2 {
  0% {
    left: 500px;
  }
  100% {
    left: -90px;
  }
}

@-webkit-keyframes cloud3 {
  0% {
    left: 620px;
  }
  100% {
    left: -70px;
  }
}
@keyframes cloud3 {
  0% {
    left: 620px;
  }
  100% {
    left: -70px;
  }
}
@-webkit-keyframes cloud4 {
  0% {
    left: 100px;
  }
  100% {
    left: -70px;
  }
}
@keyframes cloud4 {
  0% {
    left: 100px;
  }
  100% {
    left: -70px;
  }
}
</style>
