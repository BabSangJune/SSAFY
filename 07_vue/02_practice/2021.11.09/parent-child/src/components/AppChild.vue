<template>
  <div>
    <h1>App Child</h1>
    <input type="text" v-model="childData" @input="inputChild">
    <p>appData : {{appMessage}}</p>
    <p>parentData : {{parentMessage}} </p>
    <p>childData : {{childData}} </p>

  </div>
</template>

<script>
export default {
  name : 'AppChild',
  props :{
    appMessage:{
      type:String,
    },
    parentMessage:{
      type:String,
    }
  },
  data : function(){
    return{
      childData :'',
    }
  },
  methods :{
    inputChild:function(event){
      this.$emit('input-change-child', event.target.value)
    }
  }
}
</script>

<style>

</style>