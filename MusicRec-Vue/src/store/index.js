/* 2018-12-11
 *作者：qiaochaonan(cyan)
 *功能：
 */
import Vue from 'vue'
import Vuex from 'vuex'
import vuexlogin from './modules/login'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    vuexlogin
  }
})
