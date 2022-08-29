import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import Dict from './Screens/App_sul';
import Item from './Screens/App_item';

const HomeScreen = ({navigation}) => {
    return (
      <View style={styles.screen}>
        <Text>홈 화면</Text>
        <Button
          title="전체 메뉴로 이동"
          onPress={ () => navigation.navigate('전체 메뉴')}
        />
      </View>
    )
  }

const DetailsScreen = ({navigation}) => {
    return (
      <View style={styles.screen}>
        <Text>전체 메뉴</Text>
        <Button
          title="홈"
          onPress={ () => navigation.push('홈')}
        />
        <Button 
          title="전통주 사전"
          onPress={ () => navigation.navigate('전통주 사전')}
        />
        <Button
          title="뒤로 가기"
          onPress={() => navigation.goBack()}
        />
      </View>
    )
  }

const Stack = createStackNavigator();

const StackNavigation = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen name='홈' component={HomeScreen} />
            <Stack.Screen name='전체 메뉴' component={DetailsScreen} />
            <Stack.Screen name='전통주 사전' component={Dict} />
            <Stack.Screen name='상세 설명' component={Item} />
        </Stack.Navigator>  
    );
};

const styles = StyleSheet.create({
    screen: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center'
    }
  })

export default StackNavigation;