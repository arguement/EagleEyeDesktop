export var store = {
    state: {
        Index: 0,
        User: []
    },
    addIndex(newIndex) {
        this.state.Index = newIndex
    },
    addUser(newUser) {
        this.state.User = newUser
    },
    mutations: {
        replace (Index) {
            this.state.Index = Index
        }
    }
}