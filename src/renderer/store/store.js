export var store = {
    state: {
        Index: 0
    },
    addIndex(newIndex) {
        this.state.Index = newIndex
    },
    mutations: {
        replace (Index) {
            this.state.Index = Index
        }
    }
}