import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  islog:false
  },
  mutations: {
	  setLog(state,b){
		  state.islog=b;
	  }
  },
  actions: {
  },
  modules: {
  }
})
