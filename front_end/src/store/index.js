import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        isCollapse: false,
        cusname:"",
        logintime:"",
    },
    mutations:{
        collapsemenu(state){
            state.isCollapse = !state.isCollapse;
        },
        setlogintime(state, newtime){
            state.logintime = newtime
        },
        setcusname(state, newname){
            state.cusname = newname
        }
    }
})