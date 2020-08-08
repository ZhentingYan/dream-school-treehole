import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'

Vue.use(ElementUI)

Vue.config.productionTip = false
axios.defaults.withCredentials = true
Vue.prototype.$hostname =
  process.env.NODE_ENV === 'production'
    ? 'http://116.62.5.198/'
    : 'http://127.0.0.1:8000/'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
