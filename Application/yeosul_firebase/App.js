import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import StackNavigation from './navigation';

const App = () => {
    return (
        <NavigationContainer>
            <StackNavigation />
        </NavigationContainer>
    )
}

export default App;