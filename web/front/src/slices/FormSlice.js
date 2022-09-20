import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import formAPI from "@/lib/formAPI"

export const submit = createAsyncThunk(
    "forms/submit",
    async( {video, logoImage}, thunkAPI) => {
        try {
            const data = await formAPI.postSubmit(video, logoImage);
            console.log(data)
            thunkAPI.dispatch(resultAdd({result: data}))
            return data
        } catch (error) {
            console.error(error);
            return thunkAPI.rejectWithValue(error.response.data);
        }
    }
)

const initialState = { video: null, logoImage: null, isSubmitFinish: true, error: null, result: null, resultId: null }

const formSlice = createSlice({
    name: 'forms',
    initialState,
    reducers: {
        videoAdd: (state, action) => {
            state.video = action.payload.video;
        },
        logoAdd: (state, action) => {
            state.logoImage = action.payload.logoImage
        },
        resultAdd: (state, action) => {
            state.result = action.payload.result.stamp;
            state.resultId = action.payload.result.id;
        }
    },
    extraReducers: {
        [submit.pending]: (state, action) => {
            state.isSubmitFinish = false;
        },
        [submit.rejected]: (state, action) => {
            state.isSubmitFinish = true;
            state.error = action.error
        },
        [submit.fulfilled]: (state, action) => {
            state.isSubmitFinish = true;
            state.error = null;
        }
    }
});

const { actions, reducer } = formSlice;

export const { videoAdd, logoAdd, resultAdd } = actions;
export default reducer;