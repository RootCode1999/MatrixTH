//注册

<template>
  <div class="login" id="login" @keyup.enter="Reg">
    <!--    <a href="javascript:;" class="log-close"><i class="icons close"></i></a>-->
    <div class="reg-bg">
      <div class="log-cloud cloud1"></div>
      <div class="log-cloud cloud2"></div>
      <div class="log-cloud cloud3"></div>
      <div class="log-cloud cloud4"></div>

      <div class="log-logo" @click="backToHome">Welcome to MatrixTH!</div>
    </div>
    <div class="reg-email">
      <input
        type="text"
        placeholder="昵称"
        class="reg-input"
        v-model="nickname"
      />
      <input type="text" placeholder="Email" class="reg-input" v-model="mail" />

      <input
        type="password"
        placeholder="Password"
        class="reg-input"
        v-model="password"
      />
      <input
        type="password"
        placeholder="Password Again"
        class="reg-input"
        v-model="password2"
      />
      <input
        type="text"
        placeholder="verification code"
        class="findPa-input2"
        v-model="verificationCode"
      />
      <el-button
        style="width: 110px; height: 50px"
        class="primary"
        @click="askVerificationCode"
        :disabled="disabled"
      >
        {{ timeContent }}
      </el-button>
      <div class="errorMessage">{{ errorMessage }}</div>
      <a href="javascript:;" class="log-btn" @click="Reg">注册</a>
      <a href="javascript:;" class="log-btn" @click="backToLogin">返回登录</a>
    </div>
    <!--<Loading v-if="isLoging" marginTop="-30%"></Loading>-->
  </div>
</template>

<script>
// import crypto from "crypto";
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      isLoging: false,
      nickname: "",
      mail: "",
      descrip: "",
      password: "",
      password2: "",
      verificationCode: "",
      errorMessage: "", //出错提示信息
      disabled: false,
      timeContent: "发送验证码",
    };
  },
  methods: {
    //昵称格式验证
    nicknameMatching(name) {
      this.errorMessage = "";
      //昵称格式（英文昵称由1-20个字母、数字或下划线组成，中文昵称由1-7个汉字及其后的0-3个数字组成）
      let nickname_pattern =
        /^[a-zA-Z0-9_]{1,20}|[\u4e00-\u9fa5]{1,7}[0-9]{0,3}$/;
      let is_eng_name = false;
      //判断是否输入了昵称
      if (name.length == 0) {
        this.errorMessage = "请输入昵称";
        return false;
      }

      //判断是否含有英文字母，若含有认为是英文昵称
      if (name.match(/[A-Za-z]/) != null) {
        is_eng_name = true;
      }

      //如果昵称格式错误，按照情况输出错误信息
      if (nickname_pattern.test(name) == false) {
        console.log("nickname_pattern error");
        if (is_eng_name == true) {
          if (name.length > 20) {
            this.errorMessage = "英文名长度应当小于20个字符";
          } else {
            this.errorMessage = "英文名仅可由字母、数字和下划线组成";
          }
        } else {
          this.errorMessage = "中文名由1-7个汉字后跟0-3个数字组成";
        }
        return false;
      }
      console.log("nickname_pattern  pass!");
    },

    //邮件和密码的格式验证
    patternMatching2(mail, pa, pa2) {
      this.errorMessage = "";
      //Email地址
      let mail_pattern = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
      //密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)
      let password_pattern = /^\w{6,18}$/;
      if (mail_pattern.test(mail) == false) {
        console.log("mail_pattern error");
        this.errorMessage = "邮件格式错误";
        return false;
      }
      //验证两次输入的密码是否一致
      if (pa != pa2) {
        console.log("two password not same");
        this.errorMessage = "两次输入的密码不一致";
        return false;
      } else if (password_pattern.test(pa) == false) {
        console.log("password_pattern error");
        //分情况提示错误信息
        //console.log('password is '+pa);
        //console.log('password-length is:'+pa.length);

        if (pa.length < 6 || pa.length == 0) {
          this.errorMessage = "密码长度必须大于6";
        } else if (pa.length > 18) {
          this.errorMessage = "密码长度必须小于18";
        } else {
          this.errorMessage = "只能含有字母、数字、下划线";
        }

        return false;
      } else {
        return true;
      }
    },
    //验证码验证
    verify_verificationCode() {
      let _this = this;
      _this.veri_success = false;
      let verificationCode_pattern = /^[0-9]{4}$/;
      if (verificationCode_pattern.test(_this.verificationCode) == false) {
        this.errorMessage = "验证码为4位数字";
        return false;
      }
      return true;
    },

    //注册信息发送
    Reg() {
      let _this = this;
      //验证邮件地址格式和密码格式
      if (
        _this.patternMatching2(_this.mail, _this.password, _this.password2) ==
        false
      ) {
        return;
      }
      //验证昵称格式
      if (_this.nicknameMatching(_this.nickname) == false) {
        return;
      }
      //md5加密
      // const md5 = crypto.createHash("md5");
      // md5.update(_this.password);
      // let md5password = md5.digest("hex");

      //验证验证码正确性
      if (_this.verify_verificationCode() == false) {
        return;
      }
      //console.log('verificationCode verified!');
      var that = this;
      axios
        .get("/regist", {
          params: {
            username: this.nickname,
            passwd: this.password,
            ver_code: this.verificationCode,
            email: this.mail,
          },
        })
        .then(function (response) {
          console.log(response.data);
          if (response.data.status == 0) {
            that.$router.push({ path: "/Login" });
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    //发送验证码
    askVerificationCode() {
      let _this = this;
      //计时器
      if (this.timeContent == "发送验证码") {
        let time = 59;
        let timer = setInterval(() => {
          if (time > 0) {
            this.timeContent = time + "s";
            this.disabled = true;
            time--;
          } else {
            window.clearInterval(timer);
            this.disabled = false;
            this.timeContent = "发送验证码";
          }
        }, 1000);
      }
      console.log("这个就是Email:" + _this.mail);
      axios
        .get("/sendcode", {
          params: {
            email: _this.mail,
          },
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    backToLogin() {
      this.$router.push({
        path: "/login",
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
  min-height: 500px;
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

.reg-email {
  text-align: center;
  margin-top: 20px;
}
.reg-email .log-btn {
  background-color: #50e3ce;
  text-align: center;
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
.reg-input {
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
.reg-input.warn {
  border: 1px solid #f88787;
}

/* new begin */
.findPa-input2 {
  width: 255px;
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
.findPa-input2.warn {
  border: 1px solid #f88787;
}
/* new end */

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
