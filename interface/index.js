var user = JSON.parse(localStorage.getItem("user") || "{}");
var events = [];
var currentEvent = {};
window.addEventListener("DOMContentLoaded", () => {
  let buttonCreateEvent = document.getElementById("button_create_event");
  let modal = document.querySelector(".modal");
  let modalEdit = document.querySelector(".modal.edit");
  modal.addEventListener("click", ToggleModelCreateEvent);
  modalEdit.addEventListener("click", ToggleModelEditEvent);
  buttonCreateEvent.addEventListener("click", ToggleModelCreateEvent);
  if (user.id) {
    getEvents(user.email);
  }else{
    window.location.href = "login.html";
  }
});

function getEvents(email) {
  fetch(`http://localhost:3000/user/${email}`)
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      ListEvents(result);
    });
}

function Login() {
  let email = document.getElementById("email_login").value;
  fetch(`http://localhost:3000/user/${email}`)
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      user = result;
      localStorage.setItem("user", JSON.stringify(user));
      window.location.href = "index.html";
    });
}
function Signin() {
  let email = document.getElementById("email_signin").value;
  let name = document.getElementById("name_signin").value;
  let data = JSON.stringify({ email, name });
  fetch(`http://localhost:3000/user`, {
    method: "POST",
    body: data,
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      user = result;
      localStorage.setItem("user", JSON.stringify(user));
      window.location.href = "index.html";
    });
}

function createUser() {
  let email = document.getElementById("email").innerText;
  let name = document.getElementById("name").innerText;
  let data = JSON.stringify({ email, name });
  fetch("http://localhost:3000/user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: data,
  });
}

function ToggleModelCreateEvent(e) {
  let modal = document.querySelector(".modal");
  if (e.target.className == "modal") {
    return (modal.style.display = "none");
  } else {
    if (e.target.className != "modal") {
      if (modal.style.display == "none") {
        return (modal.style.display = "flex");
      }
    }
  }
}
function ToggleModelEditEvent(e) {
  let modal = document.querySelector(".modal.edit");
  if (e.target.className == "modal edit") {
    return (modal.style.display = "none");
  } else {
    if (e.target.className != "modal edit") {
      if (modal.style.display == "none") {
        return (modal.style.display = "flex");
      }
    }
  }
}

function CreateEvent() {
  let name = document.getElementById("event_name").value;
  let date = document.getElementById("event_day").value;
  let talks = document.getElementById("event_talks").value.split(",");
  let dist = document.getElementById("event_dist").value.split(",");
  let local = document.getElementById("event_local").value;
  let modal = document.querySelector(".modal");
  let data = JSON.stringify({
    date,
    talks,
    dist,
    local,
    name,
    userId: user.id,
  });

  fetch("http://localhost:3000/event", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: data,
  }).then(async()=>{
    await ListEvents()
    modal.style.display = "none"
  });
}

async function ListEvents() {
  await fetch(`http://localhost:3000/events/${user.id}`)
    .then((response) => response.json())
    .then((result) => (events = result));
  let listEvents = document.getElementById("list_events");
  let tableRows = "";

  for (let i = 0; i < events.length; i++) {
    const event = events[i];
    tableRows += `
        <tr>
          <td>${event.name}</td>
          <td>${formatDateBr(event.date)}</td>
          <td>${event.talks}</td>
          <td>${event.dist}</td>
          <td>${event.local}</td>
          <td>
            <img src="./edit.png" width="24" onclick="OpenModelEdit(${JSON.stringify(
              event
            ).replace(/"/g, "&quot;")})"/>
          </td>
        </tr>
      `;
  }

  listEvents.innerHTML = tableRows;
}
function UpdateEvent() {
  let name = document.getElementById("event_name_edit").value;
  let date = document.getElementById("event_day_edit").value;
  let talks = document.getElementById("event_talks_edit").value.split(",");
  let dist = document.getElementById("event_dist_edit").value.split(",");
  let local = document.getElementById("event_local_edit").value;
  let modal = document.querySelector(".modal.edit");
  let data = JSON.stringify({
    date,
    talks,
    dist,
    local,
    name,
    id: currentEvent.id,
  });

  fetch("http://localhost:3000/event", {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: data,
  }).then(async()=>{
    await ListEvents()
    modal.style.display = "none"
  });
}
function DeleteEvent() {
  let modal = document.querySelector(".modal.edit");
  fetch(`http://localhost:3000/event/${currentEvent.id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(async()=>{
    await ListEvents()
    modal.style.display = "none"
  });
}

function formatDate(date) {
  date = new Date(date);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}
function formatDateBr(date) {
  date = new Date(date);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${day}/${month}/${year}`;
}

function OpenModelEdit(event) {
  let modal = document.querySelector(".modal.edit");
  modal.style.display = "flex";
  currentEvent = event;
  event.date = formatDate(event.date);
  event.talks = event.talks.join(',')
  event.dist = event.dist.join(',')
  modal.innerHTML = `
      <form>
          <h2 id="modal_title">Novo Evento</h2>

          <label>Nome do evento </label>
          <input type="text" id="event_name_edit" value="${event.name}" />

          <label>Dia do evento</label>
          <input type="date" id="event_day_edit"  value="${event.date}" />

          <label>Palestrantes</label>
          <input id="event_talks_edit" type="text" value="${event.talks}" />

          <label>Públicos Alvo</label>
          <input id="event_dist_edit" type="text" value="${event.dist}" />

          <label>Local do Evento</label>
          <input id="event_local_edit" type="text"  value="${event.local}" />

          <div class="buttons">
              <button type="button" style="background-color: #f48955" onclick="DeleteEvent()">Excluir</button>
              <button type="button" onclick="UpdateEvent()">Atualizar</button>
          </div>
      </form>
  `;
}
