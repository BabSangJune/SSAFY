<template>
  <div id='app'>
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData : {{appParentData}}</p>
    <p>childData : {{appChildData}}</p>
    <br>
    <hr>
    <app-parent
      :app-message="appData"
      :parent-message="appParentData"
      :child-message="appChildData"
      @input-change-child="getChildData"
      @input-change-parent="getParentData"
    >
    </app-parent>
  </div>
</template>

<script>
// import AppChild from './components/AppChild.vue'
import AppParent from './components/AppParent.vue'


export default {
  name: 'App',
  components: {
    AppParent,
    // AppChild,
  },
  data : function () {
    return{
      appData:'',
      appParentData:'',
      appChildData:'',
    }
  },
  methods:{
    getChildData:function(appChildData){
      this.appChildData=appChildData
    },
    getParentData:function(appParentData){
      this.appParentData = appParentData
    }
  }
    
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
