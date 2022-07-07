import { configureStore, combineReducers } from '@reduxjs/toolkit';
import logger from 'redux-logger'

import formReducer from '@/slices/FormSlice'

const rootReducer = combineReducers({
    forms: formReducer,
});


export default configureStore({
  reducer: rootReducer,
  middelware: (getDefaultMiddleware) => getDefaultMiddleware({
    serializableCheck: false,
  }).concat(logger), 
  devTools: process.env.NODE_ENV !== 'production',
})