import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, Image, View, ScrollView, ActivityIndicator } from 'react-native';
import * as FileSystem from "expo-file-system";
import { Asset } from 'expo-asset';
import * as SQLite from 'expo-sqlite';
import { Dimensions } from 'react-native';
import React, { useState, useEffect } from "react";

const deviceWidth = Dimensions.get('window').width;

export default function App() {
  const [loading, setLoading] = useState("Loading...");
  const [dict, setDict] = useState([])
  function getDatabase () {
    FileSystem.downloadAsync(
      Asset.fromModule(require("./assets/database/festivals.db")).uri,
      `${FileSystem.documentDirectory}SQLite/festivals.db`
    )
      try {
        const db = SQLite.openDatabase('festivals.db')
        console.log(db);
        db.transaction(function(tx) {
            tx.executeSql(
              'SELECT * FROM festival_data;',
              [],
              function(tx, res) {
                console.log(res.rows.length);
                var temp = [];
                for (let i = 0; i < res.rows.length; ++i) {
                  temp.push(res.rows.item(i));
                }
                setDict(temp);
                setLoading("지역축제 사전");
              },
              function(tx, err) {
                console.error(err)
                // setLoading("Error!")
              }
            )
          });
      }
      catch (err) {
          console.error(err)
          // setLoading("Error!")
    }
  };
  useEffect (() => {
    getDatabase();
  }, []);

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <View style={styles.header}>
        <Text style={styles.headerText}>{ loading }</Text>
      </View>
      <ScrollView>
        {dict.length === 0 ? (
          <View style={styles.loading}>
            <ActivityIndicator color="grey" style={{marginTop: 10}} size="large" />
          </View>
        ) : (
          dict.map((item, index) =>
          <View key={index} style={styles.item}>
            <View style={styles.listContainer}>
              <Text style={styles.name}>{ item.fstvlNm }</Text>
              <Text style={styles.where}>{ item.lnmadr }</Text>
              <Text style={styles.inst}>{ item.auspcInstt }</Text>
              <Text style={styles.who}>{ item.mnnst }</Text> 
            </View>
          </View>)
        )}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff'
  },
  header: {
    // flex: 0.3,
    marginTop: 50,
    marginBottom: 20,
    alignItems: 'center',
    justifyContent: 'center'
  },
  headerText: {
    color: "black",
    fontSize: 28,
    fontWeight: "500"
  },
  loading: {
    alignItems: 'center',
    justifyContent: 'center'
  },
  item: {
    alignItems: 'center',
    justifyContent: 'center'
  },
  listContainer: {
    width: deviceWidth-20,
    borderRadius: 10,
    borderColor: "grey",
    borderWidth: 1,
    padding: 10,
    marginBottom: 10,
    color: "grey",
    backgroundColor: "white",
  },
  name: {
    color: "black",
    fontSize: 15,
    fontWeight: "bold",
    marginBottom: 5,
  },
  where: {
    color: "black",
    fontSize: 15
  },
  inst: {
    color: "black",
    fontSize: 15
  },
  who: {
    color: "black",
    fontSize: 15
  },
});
