export var store = {
    state: {
        user: [],
        admin: ''
    },
    addUser(newUser) {
        this.state.user = newUser
    },
    addAdmin(admin) {
        this.state.admin = admin
    },
    mutations: {
        changeUser(anotherUser) {
            this.state.user = anotherUser 
        },
        changeAdmin(anotherAdmin) {
            this.state.admin = anotherAdmin
        }
    }
}