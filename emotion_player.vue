<template>
  <div class="emotion-player">
    <h1>Emotion-Based Music Player</h1>
    <div class="emotion-display" :class="currentEmotion">
      <p>Your current emotion is: <strong>{{ currentEmotion }}</strong></p>
    </div>
    <div class="music-recommendations">
      <h2>Recommended Playlist:</h2>
      <ul>
        <li v-for="song in recommendedSongs" :key="song.id">{{ song.title }} - {{ song.artist }}</li>
      </ul>
    </div>
    <button @click="detectEmotion">Detect Emotion</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentEmotion: "neutral", // Default emotion
      emotions: ["happy", "sad", "angry", "relaxed", "neutral"],
      playlists: {
        happy: [
          { id: 1, title: "Happy Song 1", artist: "Artist A" },
          { id: 2, title: "Feel Good Tune", artist: "Artist B" },
        ],
        sad: [
          { id: 3, title: "Sad Melody", artist: "Artist C" },
          { id: 4, title: "Tearjerker Tune", artist: "Artist D" },
        ],
        angry: [
          { id: 5, title: "Rage Song", artist: "Artist E" },
          { id: 6, title: "Hard Beat", artist: "Artist F" },
        ],
        relaxed: [
          { id: 7, title: "Chill Vibes", artist: "Artist G" },
          { id: 8, title: "Soothing Sounds", artist: "Artist H" },
        ],
        neutral: [
          { id: 9, title: "Background Beats", artist: "Artist I" },
          { id: 10, title: "Calm Tune", artist: "Artist J" },
        ],
      },
      recommendedSongs: [],
    };
  },
  methods: {
    detectEmotion() {
      // Simulate emotion detection logic
      const randomIndex = Math.floor(Math.random() * this.emotions.length);
      this.currentEmotion = this.emotions[randomIndex];
      this.updatePlaylist();
    },
    updatePlaylist() {
      // Update recommended songs based on current emotion
      this.recommendedSongs = this.playlists[this.currentEmotion];
    },
  },
};
</script>

<style scoped>
.emotion-player {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}
.emotion-display {
  padding: 10px;
  margin: 20px 0;
  border-radius: 8px;
  color: white;
}
.emotion-display.happy {
  background-color: #ffeb3b;
  color: black;
}
.emotion-display.sad {
  background-color: #2196f3;
}
.emotion-display.angry {
  background-color: #f44336;
}
.emotion-display.relaxed {
  background-color: #4caf50;
}
.emotion-display.neutral {
  background-color: #9e9e9e;
}
.music-recommendations ul {
  list-style-type: none;
  padding: 0;
}
.music-recommendations li {
  margin: 5px 0;
}
button {
  padding: 10px 20px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #3700b3;
}
</style>
