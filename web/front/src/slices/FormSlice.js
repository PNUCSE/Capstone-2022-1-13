import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import formAPI from "@/lib/formAPI"

export const submit = createAsyncThunk(
    "forms/submit",
    async( {video, logoImage}, thunkAPI) => {
        try {
            const response = await formAPI.postSubmit(video, logoImage);
            console.log(response)
            return response
        } catch (error) {
            console.error(error);
            return thunkAPI.rejectWithValue(error.response.data);
        }
    }
)

const initialState = { video: null, logoImage: null }

const formSlice = createSlice({
    name: 'forms',
    initialState,
    reducers: {
        videoAdd: (state, action) => {
            state.video = action.payload.video;
        },
        logoAdd: (state, action) => {
            state.logoImage = action.payload.logoImage
        }
    },
    extraReducers: {
        [submit.rejected]: (state,action) => {

        },
        [submit.fulfilled]: (state, action) => {
            
        }
    }
});

const { actions, reducer } = formSlice;

export const { videoAdd, logoAdd } = actions;
export default reducer;