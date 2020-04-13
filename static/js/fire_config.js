import firebase from "firebase/app";

// Add the Firebase services that you want to use
import "firebase/auth";
import "firebase/firestore";



firebase.initializeApp({
    apiKey: "AIzaSyBQ-177bOc9oYcFYkkEFIWCGM9sPBOQgJ8",
    authDomain: "capstone-5515a.firebaseapp.com",
    databaseURL: "https://capstone-5515a.firebaseio.com",
    projectId: "capstone-5515a",
    storageBucket: "capstone-5515a.appspot.com",
    messagingSenderId: "1029326192567",
    appId: "1:1029326192567:web:a45a3faa83bfefe6437232",
    measurementId: "G-3QL74N87GF"
  })


const db = firebase.firestore();

export {db};