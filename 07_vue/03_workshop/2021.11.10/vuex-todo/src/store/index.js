import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    todos: [],
  },

  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },

    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },

    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          return {
            // todo: todoItem.title,
            ...todo,
            isCompleted: !todo.isCompleted
          }
        } else {
          return todo
        }
      })
    },
  },

  actions: {
    // createTodo(context, todoItem)
    createTodo({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },

    deleteTodo({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },

    updateTodoStatus({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },

  getters: {
    completedTodosCount(state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    },
  },

  modules: {
  },

})
