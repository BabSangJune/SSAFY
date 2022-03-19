<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span
          @click="updateTodoStatus(todo)"
          :class="{ 'is-completed': todo.is_completed }"
        >
          {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TodoList",
  data: function () {
    return {
      todos: null,
    };
  },
  methods: {
    // getTodos 발생 시
    getTodos: function () {
      axios({
        // 아래에서 가지고오기
        method: "get",
        url: "http://127.0.0.1:8000/todos/",
      })
        // 통신한 데이터를 todos에 넣는다
        .then((res) => {
          console.log(res);
          this.todos = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteTodo: function (todo) {
      axios({
        // 아래에서 가지고오기
        method: "delete",
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
      })
        .then((res) => {
          console.log(res);
          // 삭제되면 getTodos 호출
          this.getTodos();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateTodoStatus: function (todo) {
      const todoItem= {
        // spead operator로 todo 다 들고오고 is_completed는 추가 정의
        ...todo,
        is_completed: !todo.is_completed,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
      })
        .then(res => {
          console.log(res)
          // 위에 html 토클
          todo.is_completed = !todo.is_completed
        })

    },

  },
  // life cycle created 이용 페이지 render 전 getTodos 실행
  created: function () {
    this.getTodos();
  },
};
</script>

<style scoped>
.todo-btn {
  margin-left: 10px;
}

.is-completed {
  text-decoration: line-through;
  color: rgb(112, 112, 112);
}
</style>
