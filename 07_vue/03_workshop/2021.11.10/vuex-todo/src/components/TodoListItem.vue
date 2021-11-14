<template>
  <div id="todo-list-item">
    <span 
      @click="updateTodoStatus(todo)"
      :class="{ 'is-completed': todo.isCompleted }"
    >{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Del</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus'
    ])
  }
}
</script>

<style scope>
  .is-completed {
    text-decoration: line-through;
  }
</style>