let todos = document.getElementById('todos');
let data = [];
let api = 'http://127.0.0.1:8000/todos';
let addBtn = document.getElementById('add');
let titleInput = document.getElementById('new-title');
let descInput = document.getElementById('new-desc');

addBtn.addEventListener('click', (e) => {
  e.preventDefault();
  postTodo();

  //close modal
  let modal = document.getElementById('add');
  modal.setAttribute('data-bs-dismiss', 'modal');
});

let postTodo = () => {
  const title = titleInput.value;
  const description = descInput.value;

  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 201) {
      const newTodo = JSON.parse(xhr.responseText) || [];
      data.push(newTodo);
      console.log(data);
      renderTodos();
    }
  };

  xhr.open('POST', api, true);
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

  xhr.send(JSON.stringify({ title, description }));
};

let getTodos = () => {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      data = JSON.parse(xhr.responseText) || [];
      console.log(data);
      renderTodos();
    }
  };

  xhr.open('GET', api, true);

  xhr.send();
};

let renderTodos = () => {
  todos.innerHTML = '';
  data
    .sort((a, b) => b.id - a.id)
    .map((x) => {
      return (todos.innerHTML += `
        <div id="todo-${x.id}" class="todo">
            <div class="fw-bold fs-4">${x.title}</div>
            <div class="ps-3 text-secondary">${x.description}</div>
        </div>
        `);
    });
};

(() => {
  getTodos();
})();
