from df.enhance import enhance, init_df, load_audio, save_audio


if __name__ == "__main__":
    # Load default model
    model, df_state, _ = init_df(model_base_dir='../models/base')
    # Download and open some audio file. You use your audio files here
    audio_path = './jys.wav'
    audio, _ = load_audio(audio_path, sr=df_state.sr())
    # Denoise the audio
    enhanced = enhance(model, df_state, audio)
    # Save for listening
    save_audio("enhanced.wav", enhanced, df_state.sr())
