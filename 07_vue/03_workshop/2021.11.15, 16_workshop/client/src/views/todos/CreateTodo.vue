<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      // 위 모델과 양방향
      title: null,
    }
  },
  methods: {
    // 해당 이벤트 발생 시 콜백
    createTodo: function () {
      // 위 data 정의하고
      const todoItem = {
        title: this.title,
      }
      // todoItem이 값이 있을 때
      if(todoItem) {
        axios({
          // 아래로 통신
          method:'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem
        })
          .then(res => {
            console.log(res)
            // todo 생성시 router를 통해 TodoList로 가기
            this.$router.push({ name: 'TodoList' })
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  },
}
</script>
