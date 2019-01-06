// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import animate from 'animate.css'
import './assets/style/common.less'
import commontool from './assets/js/tool'
import store from './store'
import layer from 'vue-layer'
Vue.prototype.$layer = layer(Vue)
Vue.use(commontool)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
