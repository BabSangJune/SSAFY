<template>
  <div>
    <h1>lunch</h1>
    <h2>오늘의 점심은 ?</h2>
    <button @click="getLunch">점심 뽑기</button>
    <p>{{ lunchMenu }}</p>
  </div>
  
</template>

<script>
import _ from 'lodash'

export default {
  name: 'lunch',
  data: function () {
    return {
      lunchMenu: '',
    }
  },
  methods: {
    getLunch: function() {
      const lunchs = _.sample(["곰탕", "오리탕", "감자탕", "사리곰탕"])
      this.lunchMenu = lunchs
    }
  }

}
</script>

<style>

</style>