<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="AppParent" @input="inputParent">
    <p> appData : {{ appMessage }}</p>
    <p> childData : {{ childMessage }} </p>
    <br><hr>
    <app-child
      :app-message="appMessage"
      :parent-message="parentMessage"
      @input-change-child="getChildData"
    >
    </app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name : 'AppParent',
  components:{
    AppChild,
  },
  props:{
    appMessage :String,  
    childMessage : String, 
    parentMessage : String,
  },
  data : function(){
    return{
      AppParent : '',
      // appChildData:'',

    }
  },
  methods :{
    getChildData:function(appChildData){
      // this.appChildData = appChildData
      this.$emit('input-change-child', appChildData)
    },
    inputParent:function(event){
      this.$emit('input-change-parent', event.target.value)
    }

  }
}
</script>

<style>

</style>