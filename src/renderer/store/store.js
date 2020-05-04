export var store = {
    state: {
        user: []
    },
    addUser(newUser) {
        this.state.user = newUser
    },
    mutations: {
        changeUser(anotherUser) {
            this.state.user = anotherUser 
        }
    }
}