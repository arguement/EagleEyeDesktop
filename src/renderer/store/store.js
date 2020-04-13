export var store = {
    state: {
        User: []
    },
    addUser(newUser) {
        this.state.User = newUser
    },
    mutations: {
        changeUser(anotherUser) {
            this.state.User = anotherUser 
        }
    }
}