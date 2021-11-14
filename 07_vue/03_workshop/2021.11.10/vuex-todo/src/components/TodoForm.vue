<template>
  <div id="todo-form">
    <input 
      type="text" 
      @keyup.enter="createTodo" 
      v-model.trim="todoTitle"
    >
    <button @click="createTodo">create</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },

  methods: {
    createTodo() {
      const todoItem ={
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }

      if(todoItem.title) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = null
    }
  },

}
</script>

<style>

</style>