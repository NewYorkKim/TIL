import { firebase } from "./firebase"
import * as FileSystem from "expo-file-system";
import { Asset } from 'expo-asset';
import * as SQLite from 'expo-sqlite';

export const sulCollection = firebase.firestore().collection("thesool");

export function getSulData({sul_name, sul_type, sul_material, 
                            sul_alcohol, sul_capacity, sul_img,
                            sul_prize, sul_etc, sul_detail_info,
                            sul_match_food, distillery_name, distillery_address,
                            distillery_hompage, distillery_phone}) {
                                return sulCollection.doc("sul_data").set({
                                    sul_name, sul_type, sul_material, 
                                    sul_alcohol, sul_capacity, sul_img,
                                    sul_prize, sul_etc, sul_detail_info,
                                    sul_match_food, distillery_name, distillery_address,
                                    distillery_hompage, distillery_phone
                                });
};

export function getDatabase() {
    FileSystem.downloadAsync(
      Asset.fromModule(require("./assets/database/thesool.db")).uri,
      `${FileSystem.documentDirectory}SQLite/thesool.db`
    )
      try {
        const db = SQLite.openDatabase('thesool.db')
        console.log(db);
        db.transaction(function(tx) {
            tx.executeSql(
              'SELECT * FROM sul_data;',
              [],
              function(tx, res) {
                console.log(res.rows.length);
                for (let i = 0; i < res.rows.length; ++i) {
                  temp.push(res.rows.item(i));
                  getSulData({
                    sul_name: res.rows.item(i).sul_name,
                    sul_type: res.rows.item(i).sul_type,
                    sul_material: res.rows.item(i).sul_material,
                    sul_alcohol: res.rows.item(i).sul_alcohol,
                    sul_capacity: res.rows.item(i).sul_capacity,
                    sul_img: res.rows.item(i).sul_img,
                    sul_prize: res.rows.item(i).sul_prize,
                    sul_etc: res.rows.item(i).sul_etc,
                    sul_detail_info: res.rows.item(i).sul_detail_info,
                    sul_match_food: res.rows.item(i).sul_match_food,
                    distillery_name: res.rows.item(i).distillery_name,
                    distillery_address: res.rows.item(i).distillery_address,
                    distillery_hompage: res.rows.item(i).distillery_hompage,
                    distillery_phone: res.rows.item(i).distillery_phone,
                    })
                }
            },
            function(tx, err) {
                console.error(err)
                }
            )
        });
    }
    catch (err) {
        console.error(err)
    }
};