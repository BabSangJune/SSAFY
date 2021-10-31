    // form 변수에  class addList 할당 
    const form = document.querySelector('.addList')
    // addTodo 변수에 event 함수
    const addTodo = function (event) {
      // form 에서 a태그의 action 작동 안하도록 이벤트 취소 
      event.preventDefault()

      const input = document.querySelector('[name=writeTodo]')
      const content = input.value
  
      if (content.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = content

        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag) 

      } else {
        alert('할 일을 입력해주세요!')
      }
      
      event.target.reset()
    }

    form.addEventListener('submit', addTodo)