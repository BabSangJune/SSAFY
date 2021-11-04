var todoContent = new Vue ({
  el: "#todoContent",

  data: {
    content: "",

  },

  methods: {
    contentTodo() {
      this.content = event.target.value
    }
  },
})

var todoInput = new Vue ({
  el: "#todoInput",

  data:{
    content: todoContent.content

  },

  methods: {
    todoInput() {
      const todo ={
        content: todoContent.content,
        isOk: false,
      }
      listTodo.todos.push(todo)
      todoContent.content = null
    }
  }
})

var listTodo = new Vue ({
  el: "#listTodo",
  data: {
    todos: [],

  },

})