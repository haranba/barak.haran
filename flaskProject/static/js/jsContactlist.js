fetch("https://reqres.in/api/users?page=2").then(response => response.json()).then(responseJSON => createUsersList(responseJSON.data)).catch(err => console.log(err));

function createUsersList(users) {
    console.log(users);
    const curr = document.querySelector("main");

    for (let user of users) {
        const section = document.createElement("section");
        section.innerHTML = `
        <ul class="columns" data-columns="2">
        <img src ="${user.avatar}" alt="profile picture"/>
        <br>
        <span>${user.first_name}   ${user.last_name}</span>
            <br>
            ${user.email}
         <br><br>
        </ul>
        `;
        curr.appendChild(section);
    }
}