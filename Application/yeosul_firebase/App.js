import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList, ActivityIndicator } from 'react-native';
import React, { useState, useEffect } from "react";
import firebase  from './firebase';
import { object } from 'yup';

export default function App() {
  const [loading, setLoading] = useState("Loading...");
  const [sulList, setSulList] = useState({});
  const sulCollection = firebase.collection("sool");
  function getSulDocs () {
    var temp = {};
    sulCollection.get().then(docs => {
      docs.forEach((doc) => {
        temp[Object.keys(doc.data())] = Object.values(doc.data());
      });
    });
   setSulList(temp);
   setLoading("전통주 사전");
   console.log(Object.keys(sulList).length);
  }

  useEffect(() => {
    getSulDocs();
  }, []);

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <View style={styles.header}>
        <Text style={styles.headerTExt}>{ loading }</Text>
      </View>
      {/* <FlatList 
        data={Object.keys(sulList)}
        renderItem={({ item }) => <Text>{obj[item].name}</Text>}>
      </FlatList> */}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    marginTop: 50,
    marginBottom: 20,
    alignItems: 'center',
    justifyContent: 'center'   
  },
  headerText: {
    color: "black",
    fontSize: 38,
    fontWeight: "500"
  },
  loading: {
    alignItems: 'center',
    justifyContent: 'center'
  },
});
