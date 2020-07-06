export const store = {
    state: {
        user: []
    },
    addUser(newUser) {
        this.state.user = newUser
    },
    addAdmin(admin) {
        this.state.admin = admin
    },
    /*addReportClicked(newReportClicked) {
        this.state.reportClicked = newReportClicked
    },*/

    mutations: {
        changeUser(anotherUser) {
            this.state.user = anotherUser 
        },
        changeAdmin(anotherAdmin) {
            this.state.admin = anotherAdmin
        },/*
        changeReportClicked(anotherReportClicked) {
            this.state.reportClicked = anotherReportClicked 
        }*/
        
    }
}