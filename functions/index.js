const functions = require('firebase-functions');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });
const admin = require('firebase-admin');
admin.initializeApp();
//# sourceMappingURL=index.cjs.js.map
exports.NewReport = functions.firestore.document("/Crime+Report/{documentid}").onCreate((snap,context)=>{ 
    
    let myNotification = new Notification('New Report ', {
        body: 'A new report has been Been Submitted'
                       })  
    admin.messaging().sendToDevice(snap.val(), myNotification)
})