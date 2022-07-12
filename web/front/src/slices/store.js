import { configureStore, combineReducers } from '@reduxjs/toolkit';
import logger from 'redux-logger'

import formReducer from '@/slices/FormSlice'
import videoReducer from '@/slices/VideoSlice'

const rootReducer = combineReducers({
    forms: formReducer,
    videos: videoReducer
});


export default configureStore({
  reducer: rootReducer,
  middelware: (getDefaultMiddleware) => getDefaultMiddleware({
    serializableCheck: false,
  }).concat(logger), 
  devTools: process.env.NODE_ENV !== 'production',
})