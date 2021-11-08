<template>
  <div>
    <h1>로또 번호 추첨</h1>
    <h2>{{ $route.params.lottoNum }}개의 번호를 추첨합니다</h2>
    <button @click="getNums">Pick</button>
    <p>오늘의 번호는 ?</p>
    <p>{{ selectedLuckyNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
    }   
  },

  methods: {
    getNums: function () {
      const numbers = _.range(1, 46)
      this.selectedLuckyNums = _.sampleSize(numbers, this.$route.params.lottoNum)
    }
  }
}
</script>

<style>

</style>